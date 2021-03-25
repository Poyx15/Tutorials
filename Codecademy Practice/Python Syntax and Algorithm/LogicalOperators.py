print('''Create a program that
If applicant has high income AND good Credit
they are Eligible for loan
********************************************''')

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")