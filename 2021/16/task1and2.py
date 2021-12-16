# read all input lines into lines[] and strip off trailing whitespaces
lines = [x.rstrip() for x in open("input.txt")]
line = lines[0]

hextable = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111'
}

bits = ""
for c in line:
    bits += hextable[c]

VERSION_BITS = 3
PACKETTYPE_BITS = 3
counter = 0

def getNum(nbits):
    global bits, counter
    num = 0
    for i in range(nbits):
        num *= 2
        num += int(bits[i])
    bits = bits[nbits:]
    counter += nbits
    return num

versionsum = 0

def parsePacket():
    global counter, versionsum
    version = getNum(3)
    versionsum += version
    ptype = getNum(3)
    if ptype == 4:
        num = 0
        flag = 1
        while flag == 1:
            flag = getNum(1)
            nibble = getNum(4)
            num *= 16
            num += nibble
        #if flag == 0:
        #   bits = bits[4 - (counter % 4):]
        #    counter = 0
        #    break
        #print("[NUM:", num, end="]")
        return num
    else:
        values = []
        if (getNum(1) == 0):
            len = getNum(15)
            end = counter + len
            while counter < end:
                values.append(parsePacket())
        else:
            num_sub_packets = getNum(11)
            for i in range(num_sub_packets):
                values.append(parsePacket())
        if ptype == 0: return sum(values)
        if ptype == 1:
            prod = 1
            for x in values:
                prod *= x
            return prod
        if ptype == 2: return min(values)
        if ptype == 3: return max(values)
        if ptype == 5:
            if values[0] > values[1]: return 1
            else: return 0
        if ptype == 6:
            if values[0] < values[1]: return 1
            else: return 0
        if ptype == 7:
            if values[0] == values[1]: return 1
            else: return 0


print("RESULT", parsePacket())
print("VERSIONSUM", versionsum)
