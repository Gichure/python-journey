

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as zde:
    print("Cannot divide by 0 "+zde)
except ValueError as ve:
     print("Invalid Input "+ve)