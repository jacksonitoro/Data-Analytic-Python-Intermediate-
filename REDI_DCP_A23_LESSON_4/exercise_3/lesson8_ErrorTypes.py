#Write a Python program that reads a text file and prints the contents of the file.
#Use exception handling to catch any IOError and print an error message
try:
    with open('file_code.txt', 'r') as file:
        file_content = file.read()
        print(file_content)

except IOError as e:
    print(f"An IOError occurred: {e}")

#Write a Python program that prompts the user to enter a sentence, and then counts the number of words in the sentence
#Use exception handling to catch any TypeError or ValueError that may occur and print an error message.

try:
    make_sentence = input('Enter your sentence: ')
    words = make_sentence.split()
    word_count = len(words)
    print(f'Number of words in the sentence: {word_count}')

except (TypeError, ValueError) as e: #handle TypeError or ValueError 
    print(f'An error occured: {e}') #print error message


#Write a Python program that asks the user to enter a list of numbers, and then calculates the average of those numbers.
#Use exception handling to catch any errors that may occur and print an appropriate error message.
input_numbers = input('Please enter list of numbers: ')
try:
    
    numbers = [int(x) for x in input_numbers.split()]

    #calculate the average number
    if len(numbers) > 0:
        avrge = sum(numbers)/len(numbers)
        print(f'the average of the numbers is: {avrge:.2f}')

    else:
        print('No numbers were entered.')

except ValueError as e:
    print(f'Invalid input: {e}')
