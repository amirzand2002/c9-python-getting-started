# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'. The default operation is 'add'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function using named notation passing in only the numbers 6 and 4
# Should return 10
#
# Test your function using named notation with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received
def op(a,b,ope='add'):
    if ope =='add'  :
        result = a + b
    elif ope == 'subtract' :
        result = a - b
    else:
        print("Invalid operator")
    return result

first_number = float(input("Enter first number : "))
second_number = float(input("Enter second number : "))
operator = input("you want to 'add' or 'subtract' :").lower()

result = op(a=first_number,b=second_number)
print("result of add is :", result)
result = op(a=first_number,b=second_number,ope='subtract')
print("result of subtraction is :", result)