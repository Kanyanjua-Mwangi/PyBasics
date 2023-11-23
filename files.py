
fhandle = open('words.txt', 'r')
print(fhandle.read(10))

fhand2 = open('mbox.txt', 'a')
print(fhand2)

#Backslash n \n

greet = 'Hello\nWorld'
print(greet)

openfile = open("words.txt")
for line in openfile:
    print(line)

count = 0
for line in openfile:
    count = count + 1

print('Line count:', count )

fhand = open('words.txt')
inp = fhand.read()
print(inp[:20])

for line in openfile:
    line = line.rstrip()
    if not line.startswith('Ab'):
       continue 
    print(line)

fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Ce'):
        count += 1
print(count, 'words start with Ce in', fname )

count = dict()
for line in fhandle:
    lines = line.split()
    print(lines)
    for words in lines:
        count[words] = count.get(words, 0 ) + 1
        print(count[words])

    



