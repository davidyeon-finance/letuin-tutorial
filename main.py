a = 20
b = 3
c = 'james'
d = 'mike'

def calculator(num1 : int, num2 : int) -> int :
    res = num1 + num2
    return res

def myfunction(str1, num1, str2, num2):

    result_string = str1 + str2
    result_calculation = num1 // num2

    return result_calculation, result_string

function_result = myfunction(c, a, d, b)
print(function_result)