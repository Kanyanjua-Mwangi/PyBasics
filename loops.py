#while condition:
    #to do statements

x = 0
while x < 10:
    print(x)

    x = x + 1

top_100 = list(range(0, 100))
print(top_100)

for num in top_100:
    if num <=28:
        pass

print(num)

top_100_squared = [num**2 for num in top_100]

print(top_100_squared)

def top_100_even_squared():

    for num in top_100_squared:
     if num % 2 == 0:
        value = num**2
        top_100_squared.append(value)
    else:
        top_100_squared.append(num)

top_100_even_squared