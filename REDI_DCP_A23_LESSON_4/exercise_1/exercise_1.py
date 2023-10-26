set_1 = {"A", "B", "E", "J", "L", "O", "K", "Y", "N"}
set_2 = {"c", "B", "D", "N", "P", "Y", "A", "J", "M"}

# 1. Print the common elements in both sets
# Result: {'Y', 'A', 'N', 'J', 'B'}
<<<<<<< HEAD
commElement = set_1.intersection(set_2)
print(commElement)
exp_result={'Y', 'A', 'N', 'J', 'B'}
print(commElement==exp_result)
# 2. Print total number of unique elements from both sets
# Result: 13
uniq_element = set_1.union(set_2)
all_uniq_element=len(uniq_element)
print(uniq_element)
print(all_uniq_element)

# 3. Print alphabets that are in set2 but not in set1
# Result: {'c', 'P', 'D', 'M'}

diff_inset = set_2.difference(set_1)
print(diff_inset)
=======
print(set_1.intersection(set_2))


# 2. Print total number of unique elements from both sets
# Result: 13
print(len(set_1.union(set_2)))

# 3. Print alphabets that are in set2 but not in set1
# Result: {'c', 'P', 'D', 'M'}
print(set_2.difference(set_1))
>>>>>>> 62be41add9d3189d4ffd1faa885dfff2097219c6
