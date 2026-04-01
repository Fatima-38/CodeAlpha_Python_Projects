import csv
import os

# ─────────────────────────────────────────────
#  TASK 2 — Stock Portfolio Tracker
# ─────────────────────────────────────────────

def stock_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 185,
        "MSFT": 420,
        "META": 500,
        "NFLX": 630,
    }

    print("=" * 45)
    print("       📈 Stock Portfolio Tracker")
    print("=" * 45)
    print(f"\nAvailable stocks: {', '.join(stock_prices.keys())}")
    print("Type 'done' when finished.\n")

    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print(f"⚠ '{stock}' not found. Available: {', '.join(stock_prices.keys())}")
            continue

        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            if qty <= 0:
                print("⚠ Quantity must be a positive number.")
                continue
        except ValueError:
            print("⚠ Invalid quantity. Please enter a number.")
            continue

        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty

        print(f"✅ Added {qty} shares of {stock} @ ${stock_prices[stock]}/share")

    if not portfolio:
        print("\n⚠ No stocks added. Exiting.")
        return

    # Display summary
    print("\n" + "=" * 45)
    print(f"{'Stock':<10} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("-" * 45)

    total = 0
    rows = []
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        print(f"{stock:<10} {qty:>6} ${price:>9} ${value:>11,}")
        rows.append([stock, qty, price, value])

    print("=" * 45)
    print(f"{'TOTAL INVESTMENT':>38} ${total:>9,}")
    print("=" * 45)

    # Optional: save to CSV
    save = input("\nSave portfolio to CSV? (yes/no): ").lower().strip()
    if save in ("yes", "y"):
        filename = "portfolio.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
            writer.writerows(rows)
            writer.writerow([])
            writer.writerow(["", "", "Grand Total", f"${total:,}"])
        print(f"✅ Portfolio saved to '{filename}'")

stock_tracker()