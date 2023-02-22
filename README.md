<a name="readme-top"></a>
<br />

<div align="center">
  <a href="https://github.com/BarendPotijk/visualize_crypto_options/">
    <img src="Images/deribit.png" alt="Logo" width="80" height="80">
  </a>
<h3 align="center">Visualize Crypto Option trades</h3>
  <p align="center">
    A Python script for visualizing cryptocurrency option trades using the Deribit API v2
    <br />
    <a href="https://github.com/BarendPotijk/visualize_crypto_options/"><strong>Explore the docs »</strong></a>
  </p>
</div>

## Introduction ##
The visualize_crypto_options repository provides a Python script for visualizing cryptocurrency (BTC, ETH, SOL, USDC) options traded on the Deribit cryptocurrency derivative platform. The script uses the publicly available Deribit API v2.1.1 to gather option trade data and create interactive visualizations using the Plotly library.

## Project details ##
All crypto option trades since the inception of the Deribit platform are publicly available in the Deribit API v2.1.1 under https://history.deribit.com/api/v2/public/get_last_trades_by_currency. For further information and the documentations see https://docs.deribit.com/#public-get_last_trades_by_currency_and_time.

The script provides two functions for visualizing option trade data:
```python
iv_smile(`option_data`, `start_date`=None, `end_date`=None): #displays the implied volatility smile for a given time period.
iv_surface(`option_data`, `start_date`=None, `end_date`=None): #displays the volatility surface of all trades given the specified time period.
```

## Getting started ##
To use this script, you will need to have Python 3 and the following libraries installed:

* json
* requests
* pandas
* datetime
* plotly

To gather and visualize cryptocurrency option data using the script, follow these steps:

  1. Open the script (Option_visualization.py) in your preferred Python editor.
  2. Ensure that the required libraries are installed.
  3. Call OptionData().option_data() to gather option data for the desired time period : <br /> 
     ```python
     OptionData(`currency`, `start_date`, `end_date`).option_data() 
     ```
  5. Visualize the gathered option data using one of the two visualization functions, passing in the option data and any desired time filters.
  
## Parameters ##

| Parameter | Required | Type | Enum | Description |
| --- | --- | --- | --- | --- |
| currency | true | string | `BTC`<br /> `ETH` <br /> `SOL` <br /> `USDC`| The currency symbol|
| start_date | true | datetime object | | The earliest datetime object to return result for|
| end_date | true | datetime object | | The most recent datetime object to return result for|


## Examples ##
Here are some examples of the visualizations that can be created using the script:

* Implied volatility smiles: 

  The iv_smile function displays the implied volatility smile for a given time period.

  <div align="center">
  
    <a href="https://github.com/BarendPotijk/visualize_crypto_options/blob/main/Images/volatility_smile.png">
      <img src="Images/volatility_smile.png" width="65%", height = "65%">
    </a>
  </div>
  
* Implied volatility surface:

  The iv_surface function displays the volatility surface of all trades given the specified time period.

<div align="center">
  <a href="https://github.com/BarendPotijk/visualize_crypto_options/blob/main/Images/volatility_surface.png">
    <img src="Images/volatility_surface.png" width="65%", height = "65%">
  </a>
</div>

## Contributing ##
If you find a bug or would like to suggest an enhancement, please create an issue or submit a pull request. We welcome any contributions or feedback to make this script more useful and user-friendly for the cryptocurrency community.
