content = [int(x) for x in open("input.txt")]

count = 0
for i in range(1,len(content)-2):
    val1 = val2 = 0
    for j in range(0,3):
        val2 += content[i+j]
        val1 += content[i+j-1]
    print(val1, " ", val2)
    if val1 < val2: count += 1
print(count)
