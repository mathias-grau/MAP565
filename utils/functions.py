import pandas as pd
from pandas_datareader import data as pdr
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

yf.pdr_override()


def get_stock_data(stock_symbol, start_date, end_date, interval='1d'):
    data = pdr.get_data_yahoo(stock_symbol, start=start_date, end=end_date, interval=interval)
    # preprocess
    data = data.dropna()
    data = data.reset_index()
    data = data.rename(columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Adj Close': 'adj_close', 'Volume': 'volume'})
    data = data[['date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']]
    data['date'] = data['date'].dt.strftime('%Y-%m-%d')
    data['date'] = pd.to_datetime(data['date'])
    return data

def get_hourly_stock_data(stock_symbol, start_date, end_date, interval = '30m'):
    data = pdr.get_data_yahoo(stock_symbol, start=start_date, end=end_date, interval=interval)
    # preprocess
    data = data.dropna()
    data = data.reset_index()
    data = data.rename(columns={'Datetime': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Adj Close': 'adj_close', 'Volume': 'volume'})
    data = data[['date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']]
    data['date'] = data['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
    data['date'] = pd.to_datetime(data['date'])
    return data

def plot_stock_data(stock_data, column='close', name='Stock'):
    plt.figure(figsize=(20, 6))
    stock_data = stock_data.copy()
    plt.plot(stock_data['date'], stock_data[column], label=f'{column.capitalize()} Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{name} Price Over Time')
    plt.legend()
    # only 1/200 dates will be shown
    plt.xticks(stock_data['date'][::20], rotation=45)

def plot_multiple_stock_data(stock_data_dict, column='close'):
    plt.figure(figsize=(20, 6))
    for stock_symbol, stock_data in stock_data_dict.items():
        stock_data = stock_data.copy()
        plt.plot(stock_data['date'], stock_data[column], label=f'{stock_symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{column.capitalize()} Stock Price Over Time')
    plt.legend()
    # only 1/200 dates will be shown
    plt.xticks(stock_data['date'][::20], rotation=45)
    plt.show()

def compute_stock_returns(stock_data):
    stock_data = stock_data.copy()
    # % change
    stock_data['return'] = stock_data['close'].pct_change()
    stock_data = stock_data.dropna()
    return stock_data

def plot_stock_returns_distribution(stock_data, name = 'Stock'):
    stock_data = stock_data.copy()
    stock_data['return'] = stock_data['close'].pct_change()
    stock_data = stock_data.dropna()
    plt.figure(figsize=(20, 6))
    plt.hist(stock_data['return'], bins=100, color='blue')
    plt.xlabel('Return')
    plt.ylabel('Frequency')
    plt.axvline(stock_data['return'].mean(), color='red', linestyle='dashed', linewidth=1)
    # add std range
    plt.axvline(stock_data['return'].mean() + stock_data['return'].std(), color='green', linestyle='dashed', linewidth=1)
    plt.axvline(stock_data['return'].mean() - stock_data['return'].std(), color='green', linestyle='dashed', linewidth=1)
    plt.title(f'{name} Returns Distribution')
    
def compute_correlation_matrix(stock_data_dict):
    stock_data_dict = stock_data_dict.copy()
    stock_data_dict = {stock_symbol: stock_data['close'] for stock_symbol, stock_data in stock_data_dict.items()}
    stock_data = pd.DataFrame(stock_data_dict)
    stock_data = stock_data.pct_change()
    correlation_matrix = stock_data.corr()
    return correlation_matrix   

def plot_correlation_matrix(correlation_matrix, title='Correlation Matrix'):
    plt.figure(figsize=(7, 4))
    plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)
    plt.colorbar()
    plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
    plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
    plt.title(title)
    plt.show()

def compute_copula_correlation_matrix(stock_data_dict):
    stock_data_dict = stock_data_dict.copy()
    stock_data_dict = {stock_symbol: stock_data['close'] for stock_symbol, stock_data in stock_data_dict.items()}
    stock_data = pd.DataFrame(stock_data_dict)
    stock_data = stock_data.pct_change()
    copula_correlation_matrix = stock_data.corr(method='kendall')
    return copula_correlation_matrix

def compute_stock_volatility(stock_data, window=20):
    stock_data = stock_data.copy()
    stock_data['volatility'] = stock_data['close'].pct_change().rolling(window).std()
    return stock_data

def plot_stock_histogram(stock_data, column, name='Stock'):
    stock_data = stock_data.copy()
    stock_data = stock_data.dropna()
    plt.figure(figsize=(20, 6))
    plt.hist(stock_data[column], bins=20, color='blue')
    plt.xlabel(column.capitalize())
    plt.ylabel('Frequency')
    plt.axvline(stock_data[column].mean(), color='red', linestyle='dashed', linewidth=1)
    # add std range
    plt.axvline(stock_data[column].mean() + stock_data[column].std(), color='green', linestyle='dashed', linewidth=1)
    plt.axvline(stock_data[column].mean() - stock_data[column].std(), color='green', linestyle='dashed', linewidth=1)
    plt.title(f'{name} {column.capitalize()} Distribution')