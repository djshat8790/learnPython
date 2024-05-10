import pandas

read = pandas.read_csv("Stock.csv")

data_frame = pandas.DataFrame(read)
length = len(data_frame)
print(f"Number of rows: {length}")
print("------------------------")
Total_deposits_column = data_frame[data_frame["Action"] == "Deposit"]
Total_withdrawal_column = data_frame[data_frame["Action"] == "Withdrawal"]
Total_marketBuy_column = data_frame[data_frame["Action"] == "Market buy"]
Total_marketSell_column = data_frame[data_frame["Action"] == "Market sell"]
total_amount_market_buy = Total_marketBuy_column["Total"].sum()
total_amount_market_sell = Total_marketSell_column["Total"].sum()
actual_investment = total_amount_market_buy - total_amount_market_sell
total_result_from_selling = data_frame["Result"].sum()
total_stamp_duty = data_frame["Stamp duty reserve tax"].sum()
total_currency_conversion = data_frame["Currency conversion fee"].sum()
total_deposit_fee = Total_deposits_column["Deposit fee"].sum()
total_actual_deposit_trade_account = Total_deposits_column["Total"].sum()
total_deposit_from_bank = Total_deposits_column["Total"].sum() + abs(Total_deposits_column["Deposit fee"].sum())
total_withdrawn = Total_withdrawal_column["Total"].sum()
total_profits = total_result_from_selling - total_stamp_duty - total_currency_conversion


print(f"Total money from bank to trading account: {round(total_deposit_from_bank, 2)}")
print(f"Total_amount_withdrawn: {total_withdrawn}")
print("------------------------")
print(f"Total stamp duty tax: {total_stamp_duty}")
print(f"Total currency conversion fee: {round(total_currency_conversion, 2)}")
print("------------------------")
print(f"Total value after sell: {total_result_from_selling}")
print(f"Total fee and tax paid: {round(total_stamp_duty + total_currency_conversion, 2)}")
print(f"Total gain: {round(total_profits, 2)}")
print("------------------------")
print(f"Total investment at buy: {round(total_amount_market_buy, 2)}")
print(f"Total investment at sell: {total_amount_market_sell}")
print(f"Actual investment: {round(actual_investment+total_profits, 2)}")





