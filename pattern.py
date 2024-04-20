#  Creating a pattern using if-else statements

for x in range(1, 10):
    if x <= 5:
        print('*' * x)  # Upper half

    else:
        print('*' * (10 - x))  # Lower half
