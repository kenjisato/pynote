# condition_input.py

raw_input = input('Enter income: ')
income = int(raw_input)

if income < 10 ** 6:
    tax_rate = 0.0
elif income < 5 * 10 ** 6:
    tax_rate = 0.1
elif income < 10 ** 7:
    tax_rate = 0.2
else:
    tax_rate = 0.3

print('tax rate is', tax_rate)