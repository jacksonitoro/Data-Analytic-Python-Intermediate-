#EXERCISES
#function that accept list of numbers and sum the numbers
# list_num=[2,3,6,7,4]
# print(sum(list_num))

# #function that takes and returns the highest number
# list_num=[2,3,6,7,4]
# print(max(list_num))

# #list of fruits and use of insert function

# fruits_list = []
# fruits_list.insert(0, 'ananas')
# fruits_list.insert(1, 'orange')
# print(fruits_list)

# #list of fruits and use of append function
# fruits_list.append('apple')
# fruits_list.append('grapes')
# fruits_list.sort()
# fruits_list.remove('apple')

# print(fruits_list)

# #function that takes a list and check if it is empty and return boolean
# def my_list():
#     lst1=[]
#     if len(lst1)==0:
#         return True
#     else:
#         return False
   
# print(my_list())


# #function that reverse item in a list
# lst2=['mango','banana','grapes','ananas','cherry']
# lst2.reverse()
# print(lst2)   

# #take a word from user, create a loop that reverse the string check if the word is a palindrome
# word = input("Please input a word: ").lower()
# i =  len(word) - 1
# reversed_word = ""
# while i >= 0:
#     reversed_word = reversed_word + word[i]
#     i-=1
# if reversed_word == word:
#     print("Your input word is palindrome")
    
#function that square the number in a list

# lst3 = [2,4,6,8,10,]
# square_result = []
# for i in lst3:
#     square_result.append(i**2)
   
# print(square_result)

# #program that takes number from user and calculate sum of numbers between 1 and the number

# enter_num = int(input('Enter number: '))

# print(sum(range(enter_num+1)))

#program to check prime number
# ur_number =int(input('enter your number: '))
# if ur_number > 1:
#     for i in range(2, int(ur_number/2)+1):
#         if (ur_number%i)==0:
#             print(ur_number, 'is not a prime number')
#             break
# elif (ur_number%i)!==0: 
       
#     print(ur_number, 'is a prime number')
# else:
#     print(ur_number, 'is not a prime number')

        
def square(x):
    ans= x*x
    return ans
 
square(100 )
print(square(100))

x = 'hello'
print(x.upper())


    

    


