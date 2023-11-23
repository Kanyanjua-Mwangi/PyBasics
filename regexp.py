import re

fhand = open('words.txt')
#for line in fhand:
    #line = line.strip()
    #if re.search('abb$', line):
        #print(line)

y = 'I 1 2 tatoo you 3 times 2'
x = re.findall('^I. + ?t', y)
#print(x)
#print(len(x))

data = 'From jackson.nicholas@chel.se.aa Fri Aug 25 10:22:22 2023'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

words = data.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[0])

y = re.findall('From .*@([^ ]*)', data)
print(y)

numlist = list()
for line in fhand:
    line = line.rstrip()
    stuf = re.findall('^ca ([0-9,]+)', line)
    if len(stuf) != 1: continue
    num = float(stuf[0])
    numlist.append(num)

print('Maximum:', max(numlist))




