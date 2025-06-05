
def calculate_wealth_by_year(current_welth, rate_of_return, monthly_saving, years):
    total_saving = current_welth
    for year in range(1, years+1):
        interest= total_saving*(rate_of_return/100)
        total_saving+= interest+(monthly_saving*12)
        print(f"Year {year}: Total wealth is {total_saving}")
        
    return total_saving

def calculate_years_till_freedom(current_wealth, rate_of_return, monthly_saving, target_wealth):
    total_saving= current_wealth
    years_to_freedom = 0
    while total_saving<target_wealth:
        years_to_freedom +=1
        interest= total_saving*(rate_of_return/100)
        total_saving+= interest+(monthly_saving*12)
    print(f"You reach financial freedom in {years_to_freedom} years")
    return years_to_freedom


current_wealth = 10000          # Початковий капітал
rate_of_return = 5              # Річна дохідність (%)
monthly_saving = 500            # Щомісячне заощадження
target_wealth = 100000          # Цільовий капітал

years_needed = calculate_years_till_freedom(current_wealth, rate_of_return, monthly_saving, target_wealth)
calculate_wealth_by_year(current_wealth, rate_of_return, monthly_saving, years_needed)