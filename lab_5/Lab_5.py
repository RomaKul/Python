import numpy as np
N = int(input())
M = int(input())
mas = np.arange(N*M).reshape(N,M)
mas = np.random.random((N,M))*100
print(mas)

value=float(input())
def f(z, A):
    v=(np.abs(A-z))
    ide=np.argmin(v)
    F=A.reshape(1,M*N)
    return F[0][ide]

result=f(value, mas)
print(result)

#---5.3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('lab1.jpg')
imgplot = plt.imshow(img)
plt.show()
red, blue, green = img.copy(), img.copy(), img.copy()
red[:,:, 1], red[:, :, 2] = 0, 0
plt.imshow(red)
plt.show()
blue[:, :, 0], blue[:, :, 1] = 0, 0
plt.imshow(blue)
plt.show()
green[:, :, 0], green[:, :, 2] = 0, 0
plt.imshow(green)
plt.show()
lum_img = img[:,:,0]
lum_img1 = img[:,:,0]
imgplot = plt.imshow(lum_img, clim=(0.0, 255.0))
plt.show()
imgplot = plt.imshow(np.dot(img[...,:3], [0.33, 0.33, 0.33]),  cmap="gray")
plt.show()