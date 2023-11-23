thisdict = {
    'brand' : 'ford',
    'model' : 'list',
    'year': 1960    
}

print(thisdict)

x = thisdict.get('brand')
print(x)

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1

print(ccc)

ccc['cwen'] = ccc['csev'] + 1

print(ccc)
print(ord('e'))

counts = dict()
names = ['sam', 'sue', 'mike', 'antony', 'sue', 'sam']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
    
print(counts)

if name in counts:
    x = counts[name]
else:
    x = 0