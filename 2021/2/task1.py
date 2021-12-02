depth = hpos = 0
for line in open("input.txt"):
    (cmd, val) = line.split(" ")
    val = int(val)
    if cmd == "forward": hpos += val
    if cmd == "up": depth -= val
    if cmd == "down": depth += val
print("HPOS:",hpos, ", DEPTH:", depth)
print(hpos*depth)
