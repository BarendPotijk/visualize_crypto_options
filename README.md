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

How to gather the cryptocurrency option data:
  1. Open the script in your preferred Python editor.
  2. Ensure that the required libraries are installed.
  3. Call OptionData().option_data() using the specified `currency`, `start_date` and `end_date` parameters (e.g. option_data = OptionData("BTC", dt.datetime(2023, 2, 20, 0, 0, 0), dt.datetime(2023, 2, 22, 0, 0, 0)).option_data().
  4. Run the script.

How to visualize the gathered option data:
  1. 

## Examples
The iv_smile function displays the implied volatility smile for a given 'start_date' to 'end_date':
<br />
<br />
<a href="https://github.com/BarendPotijk/visualize_crypto_options/blob/main/EXAMPLES/iv_smile.html">
  <img src="Images/implied_volatility_smile.png">
</a>
<br />
<br />
Similarly the function iv_surface displays the volatility surface of all trades given the specified time range:
<br />
<br />
<a href="https://github.com/BarendPotijk/visualize_crypto_options/blob/main/EXAMPLES/iv_surface.html">
  <img src="Images/implied_volatility_surface.png">
</a>
<br /> 
<br />
## Contributing ##
If you find a bug or would like to suggest an enhancement, please create an issue or submit a pull request.
