
num =2
num %= 14

print(num)

print(round(0.88445, 2))

num1 = "2"
num2 = "3"

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)

subjects = ["History", "Physics", "Chemistry","Maths", "English"]
subjects2 = ["Art", "Business"]

subjects.append("Swahili")
subjects.extend(subjects2)

subjects.remove("History")
subjects.pop()

removed = subjects.pop()

subjects.reverse()
subjects.sort(reverse=True)
sortedsubjects = sorted(subjects)

print(subjects)
print(sortedsubjects)
print(subjects.index("Maths"))
print("English" in subjects)

for index, subject in enumerate(subjects, start=1):
    print(index, subject)

subjectstr = ", ".join(subjects)

print(subjectstr)


numlist = [1, 17, 8373, 3, 4]
numlist2 = [900, 388, 56, 9202]
numlist2.insert(3, 7373)
numlist.append(5)
numlist.extend(numlist2)
numlist.insert(4, 6)
numlist.sort()



print(numlist)
print(min(numlist))
print(max(numlist))
print(sum(numlist))

friends = ["Mike", "Susan", "Clarence", "Nicholas Jackson", "Sue"]
friends2 = friends

friends.remove("Mike")

friends[3] = "Jameson"


print(friends)
print(friends2)

friends3 = {"Mike", "Susan", "Clarence", "Nicholas Jackson", "Sue"}
friends4 = {"Mike", "Susan", "Clarence", "Jackson", "Sue", "Jrue"}

print("Jackson" in friends3)
print(friends3.intersection(friends4))
print(friends3.difference(friends4))

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)

    total = total + value
    count = count + 1


average = total/count

print(total)
print(count)

print('Average is:', average)

##frsplit = friends3.split()
#print(frsplit)

d = {'a' : 10, 'b' : 1, 'c' : 22}
#print(d.items())
#print(sorted(d.items()))
#for (k, v) in sorted(d.items()):
    #print(k, v)

tmp = list()

for (k, v) in d.items():
    tmp.append((v, k))

tmp = sorted(tmp, reverse=True)


print(tmp)


