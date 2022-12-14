import yfinance as yf
import streamlit as st
import pandas as pd

st.title("""  
GODFRAE~s Best Stock Price App

""")
st.subheader("Shown are the stock closing price and volume of Google!")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2000-5-31', end='2025-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.container()
st.title("Closing price")
st.line_chart(tickerDf.Close)

st.container()
st.title("Volume price")
st.line_chart(tickerDf.Volume)




st.subheader("Shown are the stock closing price and volume of ServiceNow, Inc!")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'NOW'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2000-5-31', end='2025-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.container()
st.title("Closing price")
st.line_chart(tickerDf.Close)

st.container()
st.title("Volume price")
st.line_chart(tickerDf.Volume)





st.subheader("Shown are the stock closing price and volume of Amazon.com, Inc!")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AMZN'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2000-5-31', end='2025-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.container()
st.title("Closing price")
st.line_chart(tickerDf.Close)

st.container()
st.title("Volume price")
st.line_chart(tickerDf.Volume)




st.subheader("Shown are the stock closing price and volume of Johnson and Johnson!")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'JNJ'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2000-5-31', end='2025-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.container()
st.title("Closing price")
st.line_chart(tickerDf.Close)

st.container()
st.title("Volume price")
st.line_chart(tickerDf.Volume)




st.subheader("Shown are the stock closing price and volume of Alphabet Inc!")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOG'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2000-5-31', end='2025-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.container()
st.title("Closing price")
st.line_chart(tickerDf.Close)

st.container()
st.title("Volume price")
st.line_chart(tickerDf.Volume)