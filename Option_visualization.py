import requests
import json
import pandas as pd
from datetime import datetime as dt
from datetime import date, timedelta
import plotly.graph_objects as go

#Time-related functions
def datetime_to_timestamp(datetime_obj): 
    """Converts a datetime object to a Unix timestamp in milliseconds."""
    return int(dt.timestamp(datetime_obj)*1000)

def timestamp_to_datetime(timestamp): 
    """Converts a Unix timestamp in milliseconds to a datetime object."""
    return dt.fromtimestamp(timestamp/1000)
                  
class OptionData():
    
    def __init__(self, currency:str, start_date:date, end_date:date):
        """
        OptionData class constructor that initializes currency, start_date and end_date parameters.

        Parameters:
            currency (str): currency code e.g. BTC
            start_date (date): The start date of the time range (inclusive).
            end_date (date): The end date of the time range (inclusive).

        Returns:
            pandas.DataFrame: A dataframe of derivative trade data for the specified currency and time range.
        """
        
        self.currency = currency
        self.start_date = start_date
        self.end_date = end_date
    
        # Validate input arguments
        assert isinstance(currency, str), "currency must be a string"
        assert isinstance(start_date, date), "start_date must be a date object"
        assert isinstance(end_date, date), "end_date must be a date object"
        assert start_date <= end_date, "start_date must be before or equal to end_date"

    def option_data(self) -> pd.DataFrame:
        """
        Retrieves option data from Deribit API within the specified date range and currency. 

        Returns:
            pd.DataFrame: DataFrame containing option data
        """
        option_list = []
        params = {
            "currency": self.currency, 
            "kind": "option",
            "count": 10000,
            "include_old": True,
            "start_timestamp": datetime_to_timestamp(self.start_date),
            "end_timestamp": datetime_to_timestamp(self.end_date)
        }
        
        url = 'https://history.deribit.com/api/v2/public/get_last_trades_by_currency_and_time'

        # Use a session object to make requests to the API endpoint in a loop, paging through results until all data has been retrieved
        with requests.Session() as session:
            while True:
                response = session.get(url, params=params)
                response_data = response.json()
                if len(response_data["result"]["trades"]) == 0:
                    break
                option_list.extend(response_data["result"]["trades"])
                params["start_timestamp"] = response_data["result"]["trades"][-1]["timestamp"] + 1
                if params["start_timestamp"] >= datetime_to_timestamp(self.end_date):
                    break
        
        option_data = pd.DataFrame(option_list)
        option_data = option_data[["timestamp", "price", "instrument_name", "index_price", "direction", "amount", 'iv']]
        option_data["kind"] = option_data["instrument_name"].apply(lambda x: str(x).split("-")[0])
        option_data["maturity_date"] = option_data["instrument_name"].apply(lambda x: str(x).split("-")[1])
        option_data["maturity_date"] = option_data["maturity_date"].apply(lambda x: dt.strptime(x, "%d%b%y"))
        option_data["strike_price"] = option_data["instrument_name"].apply(lambda x: int(str(x).split("-")[2]))
        option_data["moneyness"] = option_data["index_price"]/option_data["strike_price"]
        option_data["option_type"] = option_data["instrument_name"].apply(lambda x: str(x).split("-")[3])
        option_data["price"] = (option_data["price"]*option_data["index_price"]).apply(lambda x: round(x,2))
        option_data["date_time"] = option_data["timestamp"].apply(timestamp_to_datetime)
        option_data["time_to_maturity"] = option_data['maturity_date'] - option_data["date_time"]
        option_data["time_to_maturity"] = option_data["time_to_maturity"].apply(lambda x: max(round(x.total_seconds()/31536000,3),1e-04))
        option_data['option_type'] = option_data['option_type'].apply(lambda x: str(x).lower())
        option_data["iv"] = round(option_data["iv"]/100,3)
        option_data["time_to_maturity"] = option_data["time_to_maturity"]*365
        option_data.drop(['timestamp'], axis=1, inplace = True)
        option_data.drop_duplicates(inplace = True)
        return option_data[['instrument_name','date_time','price', 'index_price', 'direction', 'amount', 'kind', 'time_to_maturity','strike_price', 'moneyness' ,'option_type', 'iv', 'maturity_date']]

#Figures
def iv_smile(option_data, start_date = None, end_date = None):
    option_data = option_data[option_data["time_to_maturity"]>1]
    if start_date is not None:
        option_data = option_data[option_data["date_time"].apply(lambda x: x.date()) >= start_date]
    if end_date is not None:
        option_data = option_data[option_data["date_time"].apply(lambda x: x.date()) <= end_date]
    option_data.reset_index(inplace = True, drop = True)
    fig = go.Figure()
    for maturity_date in sorted(set(option_data["maturity_date"])):
        _data = option_data[option_data["maturity_date"] == maturity_date]
        fig.add_trace(go.Scatter(
            x=_data["moneyness"],
            y=_data["iv"],
            text = _data["instrument_name"],
            customdata = _data["moneyness"],
            hovertemplate=
                "<b>%{text}</b><br><br>" +
                "Implied volatility: %{y:.3f}<br>" +
                "Time to maturity: %{x:.0f} days <br>" +
                "Moneyness: %{customdata:.3f}<br>" +
                "<extra></extra>",
            mode='markers',
            marker=dict(
                size=4,   
                opacity=0.8
            ),
        name = f"{maturity_date.date()}"))
    fig.update_layout(
        title = f"{option_data['kind'][0]} Volatility Smiles from {min(_data['date_time']).date()} to {max(_data['date_time']).date()}",
        title_x=0.5,
        legend_title_text='Maturity dates',
        xaxis_title = "Moneyness",
        yaxis_title = "Implied Volatility", 
        template = 'seaborn',
        hoverlabel = dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"))
    return fig

def iv_surface(option_data, start_date = None, end_date = None):
    option_data = option_data[option_data["time_to_maturity"]>1]
    if start_date is not None:
        option_data = option_data[option_data["date_time"].apply(lambda x: x.date()) >= start_date]
    if end_date is not None:
        option_data = option_data[option_data["date_time"].apply(lambda x: x.date()) <= end_date]
    option_data.reset_index(inplace = True, drop = True)
    fig = go.Figure()
    for maturity_date in sorted(set(option_data["maturity_date"])):
        _data = option_data[option_data["maturity_date"] == maturity_date]
        fig.add_trace(go.Scatter3d(
            x=_data["moneyness"],
            y=_data["time_to_maturity"],
            z=_data["iv"],
            text = _data["instrument_name"],
            customdata = _data["date_time"],
            hovertemplate=
                "<b>%{text}</b><br><br>" +
                "Implied volatility: %{z:.3f}<br>" +
                "Time to maturity: %{y:.0f} days <br>" +
                "Moneyness: %{x:.3f}<br>" +
                "Date: %{customdata}<br>"+
                "<extra></extra>",
            mode='markers',
            marker=dict(
                size=4, 
                opacity=0.8
            ),
        name = f"{maturity_date.date()}"))
    fig.update_layout(
        title = f"{option_data['kind'][0]} Volatility Surface from {min(option_data['date_time']).date()} to {max(option_data['date_time']).date()}",
        title_x=0.5,
        scene = dict(
            xaxis_title = "Moneyness",
            yaxis_title = "Time to maturity (days)",
            zaxis_title = "Implied Volatility"), 
        autosize=False,
        width=1000,
        height=1000,
        template = 'seaborn',
        hoverlabel = dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell")
    )

    return fig
