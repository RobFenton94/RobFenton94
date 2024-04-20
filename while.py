#  While loop calculating average attemps > 1

total = 0
count = 0

while True:
    num = int(input("Enter a number: "))

    if num == -1:
        break

    total += num
    count += 1

if count > 0:
    average = total / count
    print("Average of the numbers entered: ", average)
else:
    print("No numbers entered.")
