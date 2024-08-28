
charDict = {}

s = 'shivsoni'
n = len(s)

for i in range(n):
    if s[i] in charDict:
        charDict[s[i]] +=1
    else:
        charDict[s[i]] = 1

# print(charDict)

for key, values in charDict.items():
    print(key, values)