#program that accept list of numbers and sum the numbers
list_num=[2,3,6,7,4]
print(sum(list_num))

#function that accept list of numbers and sum the numbers
def sum_list(listNum):
    sum = 0
    for item in listNum:
        sum = sum + item

    return sum
sum_list(listNum=[2,6,9,12])
print(sum_list(listNum=[2,6,9,12]))
