
deposit_amount = float(input())
deposit_period_months = int(input())
annual_interest_rate = float(input())

monthly_interest = (deposit_amount * annual_interest_rate) / 100 / 12

final_amount = deposit_amount + (deposit_period_months * monthly_interest)
print(final_amount)


