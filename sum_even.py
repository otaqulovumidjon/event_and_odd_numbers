#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 8888
#Create a variable "sum_even" and assign it 0.
sum_even = 0
#Find the sum of the even digits in the variable "var_int".
sum_even = (1 - var_int // 1000 % 2) * (var_int // 1000)
sum_even += (1 - var_int // 100 % 10 % 2) * (var_int // 100 % 10)
sum_even += (1 - var_int // 10 % 10 % 2) * (var_int // 10 % 10)
sum_even += (1 - var_int % 10 % 2) * (var_int % 10)
print(sum_even)