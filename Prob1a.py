############################################################
# Name:
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

def calc_months_to_savings(salary, des_amount=5000, savings_rate,):
    """
    Function to calculate the number of months until a certain amount has
    been saved. Assumes savings starts at nothing and that the yearly interest
    rate is divided equally between months.
    """
    bank_interest_rate = 0.03 #yearly rate
    current_savings = 0
    months = 0
    while current_savings > des_amount:
        current_savings += current_savings * savings_rate + salary * bank_interest_rate / 12
        months += 1
    return months


if __name__ == '__main__':
    SALARY = 1000
    RATE = 0.1
    print("Saving " + str(RATE) + " of $" + str(SALARY) +":")
    print("It will take", calc_months_to_savings(SALARY, RATE), "months to save $5000 or more.")
