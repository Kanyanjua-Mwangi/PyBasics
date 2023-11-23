#Built in data types.
fruits = ['banana', 'mango', 'orange', 'apple']
print(fruits)

ages = [12, 35, 43, 32.5, 'prefer not to say']
print(ages)

size = len(ages)
print("legnth of ages list is:", size)

first_age = ages[0]
last_age = ages [-1]
sub_ages = ages [2:4]

print(first_age, last_age, sub_ages)

ages[1] = "98"
print(ages)

ages.append(('89', '66'))
ages.insert(3, '29')

print(ages)

ages.remove('29')
print(ages)

ages.pop(-1)
print(ages)

del ages[2]