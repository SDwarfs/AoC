# read all input lines into lines[] and strip off trailing whitespaces
# lines = [x.rstrip() for x in open("input.txt")]

#target area: x=175..227, y=-134..-79

x1 = 175
x2 = 227
y1 = -134
y2 = -79

# target area: x=20..30, y=-10..-5
#x1 = 20
#x2 = 30
#y1=-10
#y2 =-5

#maxy = 0
def fire(vx,vy):
    global x1, x2, y1, y2, maxy
    sx = 0
    sy = 0
    i = 0
    while True:
        i += 1
        sx += vx
        sy += vy
        #print(sx,sy,vx,vy)
        #if sy > maxy: maxy = sy
        if vx>0: vx -= 1
        elif vx<0: vx += 1
        vy -= 1
        if sx >= x1 and sx <= x2 and sy >= y1 and sy <= y2:
            return i
        if sy < y1: return -1
        if sx > x2: return -1


count = 0
for y in range(-1000,1000):
    for x in range(1,1000):
        ret = fire(x,y)
        if ret>0:
            print(count)
            count += 1
print(count)
