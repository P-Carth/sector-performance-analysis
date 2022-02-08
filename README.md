# <p align='center'> SECTOR PERFORMANCE ANALYSIS </p>

## <p align='center'> <img src="https://s27389.pcdn.co/wp-content/uploads/2021/07/how-smarter-data-analysis-can-transform-financial-planning-1013x440.jpeg.webp" height="300"/> </P>

***

## Scope
#### The goal of this project was to utilize APIs to pull ticker data from stocks, bonds, and cryptos to so we could analyze their performance over the last thousand trading days. After pulling the data from the APIs, it would then be cleaned up using pandas to only keep track of the 'close' data and then after stored using SQL. From there the data can then be pulled to analyze the returns over the past thousand trading days.


#### Our first step was to create a pseudo-code
1. Import libraries
2. Load APIs
    * Binance API
    * Alpaca API
3. Create three dataframes: Crypto, Stocks, Bonds
4. Clean the dataframes removing NAs and all columns besides date and close price
5. Integrate SQL by sending the cleaned data to postgres to easily be retrieved later



#### The chosen stock market sectors and corresponding ETF tickers are:
> - Energy = `XLE`
> - Financial Services = `XLF`
> - Real Estate = `XLRE`
> - Technology = `XLK`
> - Consumer Stables = `XLP`
> - Basic Materials = `XLB`
> - Industrial = `XLI`
> - Healthcare = `XLV`
> - Utilities = `XLU`
> - Consumer Discretionary = `XLY`
> - Communication Services = `XLC`

#### The chosen Bonds and corresponding tickers are:
> - iShares 3-7 Year Treasury Bond ETF - `IEI`
> - iShares 7-10 Year Treasury Bond ETF - `IEF`
> - iShares 10-20 Year Treasury Bond ETF - `TLH`
> - iShares 20+ Year Treasury Bond ETF - `TLT`

#### The chosen cryptocurrencies and corresponding tickers are:
> - Bitcoin - `BTC` 
> - Ethereum - `ETH`
> - Binance Coin - `BNB` 
> - Cardano - `ADA` 
> - Ripple - `XRP`
