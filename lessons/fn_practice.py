'''example functions to learn definition and calling syntax'''

def my_max(num1: int, num2: int) -> int:
    '''returns the maximum value of two numbers'''
    if num1 >= num2:
        return num1
    else:
        # num1 < num2
        return num2

max: int = my_max(1,2)
print(max)

# call: calling a function
# signature: defining a function (also specifies return type)