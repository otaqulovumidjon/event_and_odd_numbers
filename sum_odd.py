#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 9549
#Create a variable "sum_odd" and assign it 0.
sum_odd = 0
#Find the sum of the odd digits in the variable "var_int".
sum_odd = (var_int // 1000 % 2) * (var_int // 1000)
sum_odd += (var_int // 100 % 10 % 2) * (var_int // 100 % 10)
sum_odd += (var_int // 10 % 10 % 2) * (var_int // 10 % 10)
sum_odd += (var_int % 10 % 2) * (var_int % 10)
print(sum_odd)