# One-day-ahead of Indian National Rupee (INR)- US Dollar (USD) Exchange rate

This study analyzes the variation in the valuation of the Indian National Rupee (INR) against the US Dollar.
The python file 01_getdata.py scrapes the exchange rate data from /www.exchangerates.org.uk/USD-INR-exchange-rate-history.html and saves in the form of a Pandas dataframe.

'Exploratory Data Analysis.ipynb' documents detailed analysis of the data and 1-day ahead forecast. This process can be broken down into the following important parts:
1. Descriptive statistics and visualization.
2. Analysis of stationarity.
3. Various techniques of smoothing and their comparison.
4. Inducing stationarity.
5. Study of Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) to determine lags.
6. Fitting a linear Autoregressive Integrated Moving Average (ARIMA) model.
7. One-day-ahead forecast.
