content = [int(x) for x in open("input.txt")]

count = 0
for i in range(1,len(content)):
    if content[i-1] < content[i]: count += 1
print(count)
