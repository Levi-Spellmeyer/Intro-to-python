from decimal import Decimal

principal = Decimal('1000.00')
rate = Decimal('0.05')

for year in range(1,11):
    amount = principal * (1 + rate) ** year
    print(f"{year:>2}{amount:>10.2f}")

# {year:>2} uses format specifier >2 to indicate that years value should be right aligned in  a field of width 2
# field width  specifies the number of character positions to use when displaying the value
# you can left align with <

#{amount:>10.2}
# Formats amount as a floating point number (f)
# right aligned (>) in a field width of 10 
# Decimal point and two digits to the right of the decimal point .2