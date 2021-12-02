depth = hpos = aim = 0
for line in open("input.txt"):
    (cmd, val) = line.split(" ")
    val = int(val)
    if cmd == "forward":
        hpos += val
        depth += aim * val
    if cmd == "up":
        aim -= val
    if cmd == "down":
        aim += val
    #print("AIM: ", aim, ", DEPTH: ", depth, ", HPOS: ", hpos)
print("HPOS:",hpos, ", DEPTH:", depth)
print(hpos*depth)
