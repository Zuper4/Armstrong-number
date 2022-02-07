# An Armstrong number is a number that is equal to the sum of its own digits to the power of the number of digits.
# For example, 370 is an Armstrong number because 370 = 3*3*3 + 7*7*7 + 0*0*0.
# And 1634 is also an Armstrong number because 1634 = 1^4 + 6^4 + 3^4 + 4^4.


Max_number = int(input("\nThis program will list you all the Armstrong numbers from 0 to : "))


for i in range(1, Max_number + 1):
    result = 0
    j = i

    while j > 0:
        k = j % 10
        result = result + k ** len(str(i))
        j = j // 10

    if result == i:
        print(str(i))

