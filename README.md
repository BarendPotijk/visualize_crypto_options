<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/BarendPotijk/visualize_crypto_options/">
    <img src="Images/deribit.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Visualize Crypto Option trades</h3>

  <p align="center">
    Visualize Cryptocurrency option trades using Deribit API v2
    <br />
    <a href="https://github.com/BarendPotijk/visualize_crypto_options/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/BarendPotijk/visualize_crypto_options/tree/main/EXAMPLES">View examples </a>
  </p>
</div>

## Project description
The visualize_crypto_options repository visualizes cryptocurrency (BTC, ETH, SOL, USDC) options traded on the cryptocurrency derivative platform Deribit (https://www.deribit.com). 
All crypto option trades since the inception of the platform are publicly available in the Deribit API v2.1.1 under `https://history.deribit.com/api/v2/public/get_last_trades_by_currency`. 
For further information and the documentations see https://docs.deribit.com/#public-get_last_trades_by_currency_and_time. 

## Getting Started ##
To use this script, you will need to have Python 3 and the following libraries installed:

  * json
  * requests
  * pandas
  * datetime
  * plotly

## Running the Script ##

How to gather and visualize the cryptocurrency option data:
  1. Open the script (href="https://github.com/BarendPotijk/visualize_crypto_options/blob/main/Option_visualization.py">Option_visualization.py)in your preferred Python editor.
  2. Ensure that the required libraries are installed.
  3. Call OptionData(`currency`, `start_date`, `end_date`).option_data().
  4. Visualize the gathered option data using one of the following functions (the optional time can be used to filter in the intial time range):

      * iv_smile(option data, optional = `start date`, optional = `end date`)
      * iv_surface(option data, optional = `start date`, optional = `end date`)
    

## Examples
The iv_smile function displays the implied volatility smile for a given `start_date` to `end_date`:
<br />
<br />
<a href="https://github.com/BarendPotijk/visualize_crypto_options/blob/main/Images/Implied Volatility Smiles.png">
  <img src="Images/Implied Volatility Smiles.png">
</a>
<br />
<br />
Similarly the function iv_surface displays the volatility surface of all trades given the specified `start_date` to `end_date`:
<br />
<br />
<a href="https://github.com/BarendPotijk/visualize_crypto_options/blob/main/Images/Implied Volatility Surface.png">
  <img src="Images/Implied Volatility Surface.png">
</a>
<br /> 
<br />
## Contributing ##
If you find a bug or would like to suggest an enhancement, please create an issue or submit a pull request.
