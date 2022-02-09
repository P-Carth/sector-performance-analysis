#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries and dependencies
import os
import json
import requests
import numpy as np
import pandas as pd
import datetime as dt
import alpaca_trade_api as tradeapi
import plotly.express as px
import hvplot.pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:password@localhost:5432/sector_analysis_performance')
from panel.interact import interact
from panel import widgets
import seaborn as steve
import panel as pn


# ### Stock Dataframes

# In[2]:


# Define a query that select all rows from the owners table
query = "SELECT * FROM stock_ticker_close;"

# Load data into the DataFrame using the read_sql() method from pandas
stock_ticker_close_df = pd.read_sql(query, engine)

# Show the data of the new DataFrame
stock_ticker_close_df


# In[3]:


# Index Stock Dataframe
stock_ticker_close_df.set_index('Date', inplace = True)
stock_ticker_close_df.index = pd.to_datetime(stock_ticker_close_df.index)
stock_ticker_close_df.head()


# In[4]:


stock_ticker_close_df_1 = stock_ticker_close_df
stock_ticker_close_df_1


# In[5]:


stock_daily_returns = stock_ticker_close_df.pct_change()
stock_daily_returns.dropna(inplace = True)
stock_daily_returns


# In[6]:


stock_daily_returns_1 = stock_daily_returns
stock_daily_returns_1


# In[7]:


stock_daily_returns_2 = stock_daily_returns
stock_daily_returns_2


# In[8]:


stock_cumulative_returns = (1 + stock_daily_returns).cumprod() - 1
stock_cumulative_returns.head()


# In[9]:


stocks_daily_returns_mean = stock_daily_returns.mean(axis=1)
stocks_daily_returns_mean = pd.DataFrame(stocks_daily_returns_mean)
stocks_daily_returns_mean.rename(columns = {0 : 'Stock Daily Return Mean'}, inplace = True)
stocks_daily_returns_mean


# In[10]:


stocks_cumulative_returns_mean = (1 + stocks_daily_returns_mean).cumprod() - 1
stocks_cumulative_returns_mean = pd.DataFrame(stocks_cumulative_returns_mean)
stocks_cumulative_returns_mean.rename(columns = {'Stock Daily Return Mean' : 'Stock Cumulative Return Mean'}, inplace = True)
stocks_cumulative_returns_mean


# In[11]:


# Calculate the daily standard deviations of all portfolios
stocks_daily_returns_mean_std = stocks_daily_returns_mean.std()


# In[12]:


# Calculate the rolling standard deviation for all portfolios using a 21-day window
stocks_daily_returns_mean_std_roll = stocks_daily_returns_mean.rolling(window=21).std()


# ### Bond Dataframes

# In[13]:


# Define a query that select all rows from the owners table
query = "SELECT * FROM bond_ticker_close;"

# Load data into the DataFrame using the read_sql() method from pandas
bond_ticker_close_df = pd.read_sql(query, engine)

# Show the data of the new DataFrame
bond_ticker_close_df


# In[14]:


# Index Stock Dataframe
bond_ticker_close_df.set_index('Date', inplace = True)
bond_ticker_close_df.index = pd.to_datetime(bond_ticker_close_df.index)
bond_ticker_close_df.head()


# In[15]:


bond_ticker_close_df_1 = bond_ticker_close_df
bond_ticker_close_df_1


# In[16]:


bond_daily_returns = bond_ticker_close_df.pct_change()
bond_daily_returns.dropna(inplace = True)
bond_daily_returns


# In[17]:


bond_daily_returns_1 = bond_daily_returns
bond_daily_returns_1


# In[18]:


bond_daily_returns_2 = bond_daily_returns
bond_daily_returns_2


# In[19]:


bond_cumulative_returns = (1 + bond_daily_returns).cumprod() - 1
bond_cumulative_returns.head()


# In[20]:


bonds_daily_returns_mean = bond_daily_returns.mean(axis=1)
bonds_daily_returns_mean = pd.DataFrame(bonds_daily_returns_mean)
bonds_daily_returns_mean.rename(columns = {0 : 'Bonds Daily Return Mean'}, inplace = True)
bonds_daily_returns_mean


# In[21]:


bonds_cumulative_returns_mean = (1 + bonds_daily_returns_mean).cumprod() - 1
bonds_cumulative_returns_mean = pd.DataFrame(bonds_cumulative_returns_mean)
bonds_cumulative_returns_mean.rename(columns = {'Bonds Daily Return Mean' : 'Bonds Cumulative Return Mean'}, inplace = True)
bonds_cumulative_returns_mean


# In[22]:


# Calculate the daily standard deviations of all portfolios
bonds_daily_returns_mean_std = bonds_daily_returns_mean.std()


# In[23]:


# Calculate the rolling standard deviation for all portfolios using a 21-day window
bonds_daily_returns_mean_std_roll = bonds_daily_returns_mean.rolling(window=21).std()


# ### Crypto Dataframes

# In[24]:


# Define a query that select all rows from the owners table
query = "SELECT * FROM crypto_ticker_close;"

# Load data into the DataFrame using the read_sql() method from pandas
crypto_ticker_close_df = pd.read_sql(query, engine)

# Show the data of the new DataFrame
crypto_ticker_close_df


# In[25]:


# Index Stock Dataframe
crypto_ticker_close_df.set_index('Date', inplace = True)
crypto_ticker_close_df.index = pd.to_datetime(crypto_ticker_close_df.index)
crypto_ticker_close_df.head()


# In[26]:


crypto_ticker_close_df_1 = crypto_ticker_close_df
crypto_ticker_close_df_1


# In[27]:


crypto_daily_returns = crypto_ticker_close_df.pct_change()
crypto_daily_returns.dropna(inplace = True)
crypto_daily_returns


# In[28]:


crypto_daily_returns_1 = crypto_daily_returns
crypto_daily_returns_1


# In[29]:


crypto_daily_returns_2 = crypto_daily_returns
crypto_daily_returns_2


# In[30]:


crypto_cumulative_returns = (1 + crypto_daily_returns).cumprod() - 1
crypto_cumulative_returns.head()


# In[31]:


cryptos_daily_returns_mean = crypto_daily_returns.mean(axis=1)
cryptos_daily_returns_mean = pd.DataFrame(cryptos_daily_returns_mean)
cryptos_daily_returns_mean.rename(columns = {0 : 'Cryptos Daily Return Mean'}, inplace = True)
cryptos_daily_returns_mean


# In[32]:


cryptos_cumulative_returns_mean = (1 + cryptos_daily_returns_mean).cumprod() - 1
cryptos_cumulative_returns_mean = pd.DataFrame(cryptos_cumulative_returns_mean)
cryptos_cumulative_returns_mean.rename(columns = {'Cryptos Daily Return Mean' : 'Cryptos Cumulative Return Mean'}, inplace = True)
cryptos_cumulative_returns_mean


# In[33]:


# Calculate the daily standard deviations of all portfolios
cryptos_daily_returns_mean_std = cryptos_daily_returns_mean.std()


# In[34]:


# Calculate the rolling standard deviation for all portfolios using a 21-day window
cryptos_daily_returns_mean_std_roll = cryptos_daily_returns_mean.rolling(window=21).std()


# ### Stock Functions

# In[35]:


# Stock Plots
# Plot close prices
columns_stocks = ['XLB','XLC','XLE','XLF','XLI','XLK','XLP','XLRE','XLU','XLV','XLY']

# Define function to create plot
def stock_prices(ticker):
    df = pd.DataFrame(stock_ticker_close_df[ticker])
    df['50 SMA'] = df.rolling(50).mean()
    df['200 SMA'] = df[ticker].rolling(200).mean()
    return df.hvplot(ylabel = "Price USD",logy=True, height = 500, width = 1200, shared_axes = False)

def stock_interact_return():
    return interact(stock_prices, ticker = columns_stocks)


def stock_ticker_close_prices():
    return stock_ticker_close_df_1.hvplot(height = 500, width = 1200, shared_axes = False)

def stock_ticker_daily_returns():
    return stock_daily_returns.hvplot(label = 'Daily Returns of Stocks', ylabel = 'Daily Return',height = 500, width = 1200, shared_axes = False)

def stock_ticker_cumulative_returns():
    return stock_cumulative_returns.hvplot(height = 500, width = 1200, shared_axes = False)

def stock_ticker_rolling_std():
    return stock_daily_returns_1.rolling(21).std().hvplot(label = "Rolling 21 Day std of All Tickers", ylabel = "Standard Deviation",height = 500, width = 1200, shared_axes = False)

def stock_ticker_corr():
    steve.set(rc = {'figure.figsize':(15,8)})
    return steve.heatmap(stock_daily_returns_2.corr(), vmin=-1, vmax=1, annot = True, fmt='.2g')


# ### Bond Functions

# In[36]:


# Plot close prices
columns_bonds = ['IEF','IEI','TLH','TLT']

# Define function to create plot
def bond_prices(ticker):
    df = pd.DataFrame(bond_ticker_close_df[ticker])
    df['50 SMA'] = df.rolling(50).mean()
    df['200 SMA'] = df[ticker].rolling(200).mean()
    return df.hvplot(ylabel = "Price USD",logy=True, height = 500, width = 1200, shared_axes = False)

def bond_interact_return():
    return interact(bond_prices, ticker = columns_bonds)

def bond_ticker_close_prices():
    return bond_ticker_close_df_1.hvplot(height = 500, width = 1200, shared_axes = False)

def bond_ticker_daily_returns():
    return bond_daily_returns.hvplot(label = 'Daily Returns of Bonds', ylabel = 'Daily Return',height = 500, width = 1200, shared_axes = False)

def bond_ticker_cumulative_returns():
    return bond_cumulative_returns.hvplot(height = 500, width = 1200, shared_axes = False)

def bond_ticker_rolling_std():
    return bond_daily_returns_1.rolling(21).std().hvplot(label = "Rolling 21 Day std of All Tickers", ylabel = "Standard Deviation",height = 500, width = 1200, shared_axes = False)

def bond_ticker_corr():
    steve.set(rc = {'figure.figsize':(15,8)})
    return steve.heatmap(bond_daily_returns_2.corr(), vmin=-1, vmax=1, annot = True, fmt='.2g')


# ### Crypto Functions

# In[37]:


# Plot close prices
columns_cryptos = ['BTC','ETH','BNB','ADA','XRP']

# Define function to create plot
def crypto_prices(ticker):
    df = pd.DataFrame(crypto_ticker_close_df[ticker])
    df['50 SMA'] = df.rolling(50).mean()
    df['200 SMA'] = df[ticker].rolling(200).mean()
    return df.hvplot(logy=True, height = 500, width = 1200,shared_axes = False)

def crypto_interact_return():
    return interact(crypto_prices, ticker = columns_cryptos)

def crypto_ticker_close_prices():
    return crypto_ticker_close_df_1.hvplot(height = 500, width = 1200, shared_axes = False)

def crypto_ticker_daily_returns():
    return crypto_daily_returns.hvplot(label = 'Daily Returns of Cryptos', ylabel = 'Daily Return',height = 500, width = 1200, shared_axes = False)

def crypto_ticker_cumulative_returns():
    return crypto_cumulative_returns.hvplot(height = 500, width = 1200, shared_axes = False)

def crypto_ticker_rolling_std():
    return crypto_daily_returns_1.rolling(21).std().hvplot(label = "Rolling 21 Day std of All Tickers", ylabel = "Standard Deviation",height = 500, width = 1200, shared_axes = False)

def crypto_ticker_corr():
    steve.set(rc = {'figure.figsize':(15,8)})
    return steve.heatmap(crypto_daily_returns_2.corr(), vmin=-1, vmax=1, annot = True, fmt='.2g')


# ### Combined Functions

# In[59]:


def combined_daily_returns():
    return stocks_daily_returns_mean.hvplot(label = 'Mean Daily Returns of Stocks', ylabel = 'Mean Daily Return %', height = 500, width = 1000, color = 'r', shared_axes = False)* bonds_daily_returns_mean.hvplot(label = 'Mean Daily Returns of Bonds', ylabel = 'Mean Daily Return %', height = 500, width = 1000, color = 'b', shared_axes = False) * cryptos_daily_returns_mean.hvplot(label = 'Mean Daily Returns of Cryptos', ylabel = 'Mean Daily Return %', height = 500, width = 1000, color = 'g', shared_axes = False) 

def combined_cumulative_returns():
    return stocks_cumulative_returns_mean.hvplot(label = 'Mean Cumulative Returns of Stocks', ylabel = 'Mean Cumulative Return %', height = 500, width = 1000, color = 'r', shared_axes = False)* bonds_cumulative_returns_mean.hvplot(label = 'Mean Cumulative Returns of Bonds', ylabel = 'Mean Cumulative Return %', height = 500, width = 1000, color = 'b', shared_axes = False) * cryptos_cumulative_returns_mean.hvplot(label = 'Mean Cumulative Returns of Cryptos', ylabel = 'Mean Cumulative Return %', height = 500, width = 1000, color = 'g', shared_axes = False)

def combined_rolling_std():
    return stocks_daily_returns_mean_std_roll.hvplot(label = 'Rolling STD of Stock Asset Class', ylabel = 'Mean STD', height = 500, width = 1000, color = 'r', shared_axes = False, ylim = (-.02,.14))*bonds_daily_returns_mean_std_roll.hvplot(label = 'Rolling STD of Bond Asset Class', ylabel = 'Mean STD', height = 500, width = 1000, color = 'b',  ylim = (-.02,.14))*cryptos_daily_returns_mean_std_roll.hvplot(label = 'Rolling STD of Crypto Asset Class', ylabel = 'Mean STD', height = 500, width = 1000, color = 'g', ylim = (-.02,.14))


# In[55]:


combined_rolling_std()

