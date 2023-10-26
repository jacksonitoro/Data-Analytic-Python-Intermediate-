#Square the Elements: Given a list of numbers, use map to return a new list containing the square of each number.
number_list = [1,2,3,4,5]
def square(n):
    return n*n
map_obj = map(square,number_list)

print(list(map_obj))

#Capitalize Strings: Given a list of strings, use map to return a new list where each string is capitalized.
fruit_list=['apple','mango','berry']
cap_item=list(map(lambda x:x.capitalize(),fruit_list))
print(cap_item)
#alternatively
strings = ['apple','mango','berry']
cap_strings = list(map(str.capitalize,strings))
print(cap_strings)

# input_list = []
#Concatenate Strings: Given a list of strings, use reduce to concatenate them into a single string, separated by a space.
from functools import reduce
fruit_name = ['apple','banana','cherry']
concate_fruits = reduce(lambda x,y: x+''+y, fruit_name)
print(concate_fruits)

#Product of Elements: Given a list of numbers, use reduce to find the product of all the elements in the list.
# Input: [1, 2, 3, 4]
# Output: 24

num_list = [1, 2, 3, 4]
sol_product = reduce(lambda a,b:a*b, num_list)
print(sol_product)


#Filter Out Negative Numbers: Given a list of numbers, use filter to return a new list containing only the positive numbers.
# Input: [-1, 2, -3, 4, -5]
# Output: [2, 4]

given_num = [-1, 2, -3, 4, -5]
positive_num = list(filter(lambda x:x > 0, given_num))
print(positive_num)


#alternatively with def function

def pos_num(number):
    return number > 0
given_num1 = [-1, 2, -3, 4, -5, 6, -7, 8]
out_result = list(filter(pos_num,given_num1))

print(out_result)


#filter out positive numbers and return only negative numbers
given_num = [-1, 2, -3, 4, -5]
positive_num = list(filter(lambda x:x < 0, given_num))
print(positive_num)

#alternatively with def function

def pos_num(number):
    return number < 0
given_num1 = [-1, 2, -3, 4, -5, 6, -7, 8]
out_result = list(filter(pos_num,given_num1))

print(out_result)


#Filter Even-Length Strings: Given a list of strings, use filter to return a new list containing only the strings with an even length.
# Input: ['apple', 'banana', 'cherry', 'date']
# Output: ['apple', 'banana', 'date']

string_list = ['apple', 'banana', 'cherry', 'date']

even_length_string = list(filter(lambda x: len(x)%2==0,string_list))
print(even_length_string)


#for string with odd length

string_list1 = ['apple', 'banana', 'cherry', 'date', 'grape', 'fig']
odd_length_string = list(filter(lambda x: len(x)%2==1, string_list1))
print(odd_length_string)