# define the tax brackets and rates
tax_brackets = [(0, 150000, 0), (150001, 300000, 0.10), (300001, 500000, 0.20), (500001, float('inf'), 0.30)]

def calculate_tax(taxable_income):
    # iterate through the tax brackets
    for bracket in tax_brackets:
        if taxable_income <= bracket[1]:
            # calculate tax for this bracket
            tax = (taxable_income - bracket[0]) * bracket[2]
            return tax
    # if taxable income is above the highest bracket, return 0 (should not happen)
    return 0

# test the function
taxable_income = int(input("Enter taxable income: "))
tax = calculate_tax(taxable_income)
print("Tax:", tax)
