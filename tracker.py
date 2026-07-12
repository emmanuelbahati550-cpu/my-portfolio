# ==============================================================================
# APEX SOFTWARE SOLUTIONS - DAILY BUSINESS CASH TRACKER
# ==============================================================================

print("==========================================")
print("     DAILY BUSINESS EXPENSE TRACKER       ")
print("==========================================\n")

# 1. Collect Income and Expense Data via Keyboard Inputs
business_date = input("Enter current date (e.g., DD/MM/YYYY): ")
total_sales = float(input("Enter total cash collected from sales today (KES): "))

print("\nEnter your daily business operating expenses:")
rent_transport = float(input(" -> Transport / Rent / Cyber Café fees (KES): "))
internet_bundles = float(input(" -> Internet bundles / Community Wi-Fi costs (KES): "))
other_expenses = float(input(" -> Miscellaneous / Other expenses (KES): "))

# 2. Financial Calculations
total_expenses = rent_transport + internet_bundles + other_expenses
net_profit = total_sales - total_expenses

# 3. Output Financial Analysis to the Terminal Screen
print("\n" + "=" * 42)
print(f"FINANCIAL STATEMENT FOR: {business_date}")
print("=" * 42)
print(f"Gross Cash Inflow:      KES {total_sales:,.2f}")
print(f"Total Business Costs:   KES {total_expenses:,.2f}")
print("-" * 42)

if net_profit > 0:
    print(f"NET PROFIT (GAIN):      KES {net_profit:,.2f} 🚀")
elif net_profit < 0:
    print(f"NET DEFICIT (LOSS):     KES {abs(net_profit):,.2f} ⚠️")
else:
    print("Business broke even today (Zero Profit/Loss).")
print("=" * 42)

# 4. Automation Step: Append or Create a Daily Ledger Text File
ledger_filename = "Daily_Business_Ledger.txt"

with open(ledger_filename, "a") as ledger:
    ledger.write(f"Date: {business_date}\n")
    ledger.write(f" -> Total Sales:    KES {total_sales:,.2f}\n")
    ledger.write(f" -> Total Expenses: KES {total_expenses:,.2f}\n")
    ledger.write(f" -> Net Income:     KES {net_profit:,.2f}\n")
    ledger.write("-" * 40 + "\n")

print(f"\nSuccess! Daily log appended to '{ledger_filename}' on your Desktop.")
