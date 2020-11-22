first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
print("Please select the operation.")
print("1. For Addition")
print("2. For Subtraction")
print("3. For Multiplication")
print("4. For Division")
print("5. For Modulus")
print("6. For Maximum Number")
print("7. For Exponential Function")

operation = int(input("Please select the operation: "))
    


def multiply(x,y):
    return float(x) * float(y)
    
def divide(nominator, denominator):
    return float(nominator) / float(second_number);

def add(first_number, second_number):
    return float(first_number) + float(second_number);

def modulus(first_number, second_number):    
    return float(first_number) % float(second_number);

def subtract(first_number, second_number):
    return float(first_number) - float(second_number);

def max_number(first_number, second_number):
    if(first_number > second_number):
        return float(first_number)
    else:
        return float(second_number);
    
def raise_to_power(base_number, power_number):
    result = 1
    for index in range(int(power_number)):
        result = result * int(base_number)
    return result
    
print("You selected: "+str(operation)) 

if(operation == 1):
    result = add(first_number,second_number)
if(operation == 2):
    result = subtract(first_number,second_number)
elif(operation == 3):
    result = multiply(first_number,second_number)
elif(operation == 4):
    result = divide(first_number,second_number)
elif(operation == 5):
    result = modulus(first_number,second_number)
elif(operation == 6):
    result = max_number(first_number,second_number)
elif(operation == 7):
    result = raise_to_power(first_number,second_number)
else:
    result = "Unkown Operation"

print(result)