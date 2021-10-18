import yfinance as yf
import plotly.graph_objects as go


def intro():
    print("------ STOCKMARKET ------")
    print(" -- INFORMATION FINDER --")


def get_ticker() -> object:
    ticker_request = input("Please input a ticker symbol? ")
    return yf.Ticker(ticker_request.upper())


def ticker_date_int(ticker) -> object:
    time = input("Please specify a time period required? \n [1d][5d][1mo][3mo][6mo][1y][2y][5y][10y][ytd][max] \n")
    int_req = input("Please specify the interval? \n [1m][2m][5m][15m][30m][60m][90m][1h][1d][5d][1wk][1mo][3mo] \n")
    return ticker.history(period=time, interval=int_req)


def information(t):
    choice = input(
        """Please choose a category?
        [i] General information
        [s] Splits
        [f] Financials
        [b] Balance sheet
        [e] Earnings
        [c] Cashflow
        [r] Return \n"""
    )

    choice = choice.lower()
    if choice == "i":
        print(t.info)
    elif choice == "s":
        print(t.splits)
    elif choice == "f":
        print(t.financials)
    elif choice == "b":
        print(t.balance_sheet)
    elif choice == "e":
        print(t.earnings)
    elif choice == "c":
        print(t.cashflow)
    elif choice == "r":
        return True
    else:
        print("Invalid input, please try again")

    information(t)


def candlestick(t):
    fig = go.Figure()
    fig.add_trace(
        go.Candlestick(x=t.index, open=t['Open'], high=t['High'], low=t['Low'], close=t['Close'], name='market data'))
    fig.update_layout(title="Share Price", yaxis_title="Price (USD)")
    fig.show()