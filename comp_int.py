#compute compound interest of 4% on an amount
##      after num_of_yrs years

def calc_interest(initial_amount, num_of_yrs):
    amount = initial_amount
    for i in range(num_of_yrs):        
        interest = 0.04 * amount  #4% interest
        amount  += interest
    return amount

num_yrs = 6
initial_amount = 100
print(f"After {num_yrs} years you have:",
     calc_interest(initial_amount, num_yrs), "total amount")

