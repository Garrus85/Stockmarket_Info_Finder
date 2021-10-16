import services


def main():
    services.intro()
    ticker = services.get_ticker()

    while True:
        choice = input("""
    [i]  Information
    [c]  Charts
    [t]  Change ticker
    [q]  Quit
""").lower()

        if choice in ["i", "info", "information"]:
            services.information(ticker)
            continue
        elif choice in ["c", "charts", "chart"]:
            ticker_info = services.ticker_date_int(ticker)
            services.candlestick(ticker_info)
            continue
        elif choice in ["t", "ticker", "tick"]:
            main()
        elif choice in ["q", "quit"]:
            pass
        else:
            print("Invalid input.")
            continue
        break



if __name__ == "__main__":
    main()
