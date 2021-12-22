import numpy as np

filename = "s3"

map = np.zeros((101, 101, 101), 'uint8')

for line in open(filename):
    line = line.rstrip()
    # "off x=9..11,y=9..11,z=9..11"
    val, coords = line.split(" ")
    coords = coords.split(",")
    x1, x2 = coords[0].split("..")
    y1, y2 = coords[1].split("..")
    z1, z2 = coords[2].split("..")
    _, x1 = x1.split("=")
    _, y1 = y1.split("=")
    _, z1 = z1.split("=")
    if val == "on": val = 1
    else: val = 0
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)
    if (x1 >= -50 or x2 <=50) and (y1 >= -50 or y2 <= 50) and (z1 >= -50 and z2 <= 50):
        x1 = min(max(x1, -50), 50)
        x2 = min(max(x2, -50), 50)
        y1 = min(max(y1, -50), 50)
        y2 = min(max(y2, -50), 50)
        z1 = min(max(z1, -50), 50)
        z2 = min(max(z2, -50), 50)
        map[(z1+50):(z2+50+1),(y1+50):(y2+50+1), (x1+50):(x2+50+1)] = val
        print(np.sum(map), line)
print(np.sum(map))
