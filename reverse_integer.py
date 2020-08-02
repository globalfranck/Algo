# Input = positive or negative integer number
# Output = reversed integer

def reverse_int (integer):
	""" function takes an integer and return it reversed """
	
	str_int = str(integer)
	type_str = type(integer)
	len_str = len(str_int)

	reversed_num = ""

	if(type_str != int) :
		return "$$ Error value, not an integer$$"
	else:
		if str_int[0] == "-":
			reversed_num += "-"
			for i in range(len_str-1,0,-1):
				reversed_num += str_int[i]
		else:
			for i in range(len_str-1,-1,-1):
				reversed_num += str_int[i]
		return int(reversed_num)


# Unit test cases
num1 = 12354
num2 = -98765
num3 = 111001
num4 = "12"
num5 = None

# Showcasing
print(f"The reversed version of : {num1} is {reverse_int(num1)}")
print(f"The reversed version of : {num2} is {reverse_int(num2)}")
print(f"The reversed version of : {num3} is {reverse_int(num3)}")
print(f"The reversed version of : {num4} is {reverse_int(num4)}")
print(f"The reversed version of : {num5} is {reverse_int(num5)}")
