# Input = positive or negative integer number
# Output = reversed integer

def reverse_int (int_num):
	""" function takes an integer and return it reversed """
	return int_num


# Unit test cases
num1 = 123
num2 = -987
num3 = 0
num4 = "12"
num5 = None

# Showcasing

print(f"The reversed version of : {num1} is {reverse_int(num1)}")
print(f"The reversed version of : {num2} is {reverse_int(num2)}")
print(f"The reversed version of : {num3} is {reverse_int(num3)}")
print(f"The reversed version of : {num4} is {reverse_int(num4)}")
print(f"The reversed version of : {num5} is {reverse_int(num5)}")
