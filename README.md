# <p align='center'> SECTOR PERFORMANCE ANALYSIS </p>

## <p align='center'> <img src="https://s27389.pcdn.co/wp-content/uploads/2021/07/how-smarter-data-analysis-can-transform-financial-planning-1013x440.jpeg.webp" height="300"/> </P>

#### Contributors: Joseph Hagemann, Emilio Cubero, Jorge Betancourt, Preston Kirschner

## Scope
#### The goal of this project is to utilize APIs to pull ticker data from stocks, bonds, and cryptocurrencies to analyze their performance over the last thousand trading days. After pulling the data from the APIs, it would then be cleaned up using pandas to only keep track of the `close` prices and then stored them in a database using SQL. From there the data can then be pulled to analyze the returns over the past thousand trading days.

### Application
1. Used for our own comparative analytics within and across asset classes
2. Analysis notebook and corresponding dashboard can be used as a tool for any future analysis, as someone can pass in their own tickers related to each asset class

## Steps
*Data extraction, cleaning, storage:*
1. Draft Project Proposal and Excel Dashboard Roadmap
2. Import libraries and dependencies
3. Utilize API calls to create data frames for all tickers within each asset class
      * `Alpaca API`
      * `Binance API`
4. Clean the dataframes 
5. Remove Timestamp from Index
6. Drop all columns except close price for each ticker
7. Utilize SQL to write the cleaned data frames into postgres as tables to easily be retrieved later in the dashboard file

*Transformation:*
1. Plot 50-day and 200-day rolling averages of close price with dropdown selector for all tickers
2. Found daily and cumulative returns to accurately compare data by transforming the close prices
3. Plot rolling standard deviation of all tickers 
4. Plot correlation of returns within same asset classes
      * Return values to determine interdependence 
      * Plot on heatmap using Seaborn

*Dashboard:*
1. Utilize SQL to read in stored close price data frames from postgres
2. Copy/Paste transformations above
3. Define functions to return desired visualizations 




## Data Selected for Analysis
#### The chosen *stock* market sectors and corresponding ETF tickers are:
> - Energy = `XLE`
> - Financial Services = `XLF`
> - Real Estate = `XLRE`
> - Technology = `XLK`
> - Consumer Staples = `XLP`
> - Basic Materials = `XLB`
> - Industrial = `XLI`
> - Healthcare = `XLV`
> - Utilities = `XLU`
> - Consumer Discretionary = `XLY`
> - Communication Services = `XLC`

#### The chosen *bonds* and corresponding tickers are:
> - iShares 3-7 Year Treasury Bond ETF - `IEI`
> - iShares 7-10 Year Treasury Bond ETF - `IEF`
> - iShares 10-20 Year Treasury Bond ETF - `TLH`
> - iShares 20+ Year Treasury Bond ETF - `TLT`

#### The chosen *cryptocurrencies* and corresponding tickers are:
> - Bitcoin - `BTC` 
> - Ethereum - `ETH`
> - Binance Coin - `BNB` 
> - Cardano - `ADA` 
> - Ripple - `XRP`

## Strengths & Limitations
* Since we were limited to free APIs we were capped with a call of no more than 1000 rows of data per ticker. This lead to an issue we encountered while comparing data from cryptocurrencies which trade 7 days/week and stock/bonds which trade 5 days/week. As a result we only have 638 rows shared among all three asset classes: Crypto, Bonds, and Stocks. However, this is still a large enough dataset to use in our analysis.
* Git Branching
* Multi-Level index on Stocks and Bonds
* Could use better formatting for the visualiziation of our daily returns. With more time we would create a bar chart to show the variance of each ticker rather than a line graph.
* Another enhancement we would like to implement would be to exchange our fixed ticker data with an input function to easily input any ticker of interest


## Instructions for Following Along
1. The following dependencies are required: pyvizenv, sql, postgres
<p align='left'> <img src="https://github.com/P-Carth/sector-performance-analysis/blob/main/Screenshots/Screen%20Shot%202022-02-09%20at%203.39.54%20PM.png?raw=true" width="500"/> </P>

2. Download the `sector-performance-analysis` repo
3. Create a new postgres database called `sector_analysis_performance`
4. set postgres password to `password`
5. Restart and run all cells on main.ipynb
6. Restart and run all cells on dashboard.ipynb
7. Interact with dashboard to interpret analyses of tickers by asset class

### For Additional Enhancements & Extrapolation to Other `STOCK/BOND` Tickers

1. Navigate to the following snippet in the `main.ipynb` file
<p align='left'> <img src="https://github.com/P-Carth/sector-performance-analysis/blob/main/Screenshots/Screen%20Shot%202022-02-09%20at%204.02.33%20PM.png?raw=true" width="500"/> </P>

2. Set desired start and end dates
3. Replace stock_tickers with any single stock ticker or list of stock tickers
4. `Restart and Run` all cells
5. Navigate to dashboard `Restart and Run` all cells


### For Additional Enhancements & Extrapolation to Other `CRYPTO` Tickers
* *Note* This will only work if the crypto of interest is listed on Binance
1. Navigate to the following snippet in the `main.ipynb` file
<p align='left'> <img src="https://github.com/P-Carth/sector-performance-analysis/blob/main/Screenshots/Screen%20Shot%202022-02-09%20at%204.10.35%20PM.png?raw=true" width="500"/> </P>

2. Replace `BTCUSDT` with desired crypto ticker and specify corresponding ticker for dataframe
3. `Restart and Run` all cells
4. Navigate to dashboard `Restart and Run` all cells
