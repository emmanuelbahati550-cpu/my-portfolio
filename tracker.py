# ==============================================================================
# APEX SOFTWARE SOLUTIONS - DAILY BUSINESS CASH TRACKER
# ==============================================================================
from datetime import datetime

def get_valid_amount(prompt):
    """Ensures the user inputs a valid positive float number for money."""
    while True:
        try:
            amount_str = input(prompt).strip()
            # If they enter nothing, default to 0.00
            if amount_str == "":
                return 0.0
            amount = float(amount_str)
            if amount >= 0:
                return amount
            else:
                print("❌ Amount cannot be negative! Please enter a positive value.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid amount (e.g., 1500 or 150.50).")

print("==========================================")
print("     DAILY BUSINESS EXPENSE TRACKER       ")
print("==========================================\n")

# 1. Collect Date with automatic fallback to today
business_date = input("Enter current date (e.g., DD/MM/YYYY) [Or press Enter for Today]: ").strip()
if not business_date:
    business_date = datetime.today().strftime('%d/%m/%Y')

# Collect Income and Expense Data safely
total_sales = get_valid_amount("Enter total cash collected from sales today (KES): ")

print("\nEnter your daily business operating expenses (Press Enter if KES 0.00):")
rent_transport = get_valid_amount(" -> Transport / Rent / Cyber Café fees (KES): ")
internet_bundles = get_valid_amount(" -> Internet bundles / Community Wi-Fi costs (KES): ")
other_expenses = get_valid_amount(" -> Miscellaneous / Other expenses (KES): ")

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

try:
    with open(ledger_filename, "a") as ledger:
        ledger.write(f"Date: {business_date}\n")
        ledger.write(f" -> Total Sales:    KES {total_sales:,.2f}\n")
        ledger.write(f" -> Total Expenses: KES {total_expenses:,.2f}\n")
        ledger.write(f" -> Net Income:     KES {net_profit:,.2f}\n")
        ledger.write("-" * 40 + "\n")
    print(f"\n⚡ Success! Daily log appended to '{ledger_filename}' on your Desktop.")
except Exception as e:
    print(f"\n⚠️ Could not update ledger file. Error details: {e}")
