path = 'file1.txt'
data = open(path, 'r')
for line in data:
    mnohochlen1 = line.split('+')
data.close

path = 'file2.txt'
data = open(path, 'r')
for line in data:
    mnohochlen2 = line.split('+')
data.close

print(mnohochlen1)
print(mnohochlen2)
mnohochlen1 = line.split('x^')
print(mnohochlen1)

exit()
a = list(zip())
print(a)
