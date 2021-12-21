from numba import jit
import numpy as np

@jit(nopython=True)
def enhance(src, dst, img_params):
    W, H, fill = img_params
    img_params[0] += 2
    img_params[1] += 2
    img_params[2] = IEA[fill*511]
    for y in range(H+2):
        for x in range(W+2):
            idx = 0
            for ry in range(y-2,y+1):
                if ry < 0 or ry >= H:
                    for i in range(3):
                        idx = (idx<<1) + fill
                else:
                    for rx in range(x-2,x+1):
                        if rx < 0 or rx >= W:
                            idx = (idx<<1) + fill
                        else:
                            idx = (idx<<1) + src[ry][rx]
            dst[y][x] = IEA[idx]

def getLit(img, img_params):
    W, H, fill = img_params
    if fill == 1: return -1
    return np.sum(img[0:H,0:W])

N_ROUNDS=1000
f = open("i")
IEA = np.array([(0 if c=='.' else 1) for c in f.readline().rstrip()], 'int')
f.readline()
image = [[(0 if c=='.' else 1) for c in line.rstrip()] for line in f]
f.close()

W = len(image[0])
H = len(image)
fill = 0
src = np.empty((H+4*N_ROUNDS,W+4*N_ROUNDS), 'int')
dst = np.empty((H+4*N_ROUNDS,W+4*N_ROUNDS), 'int')
src[0:H,0:W] = image

img_params = np.array([W, H, fill], 'int')
for i in range(N_ROUNDS//2):
    enhance(src, dst, img_params)
    enhance(dst, src, img_params)
    if i == 0: print("PART 1:", getLit(src, img_params))
print("PART 2:", getLit(src, img_params))
