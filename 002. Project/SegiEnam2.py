print("\033c")
import numpy as np
import matplotlib.pyplot as plt

#Ukuran layar
col = int(800); row = int(800)

#Empat titik koordinat untuk persegi panjang
x1 = 169; y1 =400
x2 = 285; y2 = 200
x3 = 515; y3 = 200
x4 = 631; y4 = 400
x5 = 515; y5 = 600
x6 = 285; y6 = 600

#Diameter titik
pd = int(30)
#Lebar garis
lw = int(10)

#Menghitung diameter titik dan lebar garis
hd = int(pd/4)
hw = int(lw/4)

#Menyiapkan layar hitam
screen = np. zeros(shape=(row, col, 3), dtype=np.uint8)

#Perhitungan min dan maks
x_min = int(min(x1, x2, x3, x4, x5, x6));
x_max = int(max(x1, x2, x3, x4, x5, x6))
y_min = int(min(y1, y2, y3, y4, y5, y6));
y_max = int(max(y1, y2, y3, y4, y5, y6))

#Mewarnai titik berwarna merah dengan menggunakan perulangan dan kondisi
for i in range(x1-hd, x1+hd):
    for j in range(y1-hd, y1+hd):
        if ((i-x1)*2 + (j-y1)*2) < hd*2:
            screen[j,i,:] = 255

for i in range(x2-hd, x2+hd):
    for j in range(y2-hd, y2+hd):
        if ((i-x2)*2 + (j-y2)*2) < hd*2:
            screen[j,i,:] = 255

for i in range(x3-hd, x3+hd):
    for j in range(y3-hd, y3+hd):
        if ((i-x3)*2 + (j-y3)*2) < hd*2:
            screen[j,i,:] = 255

for i in range(x4-hd, x4+hd):
    for j in range(y4-hd, y4+hd):
        if ((i-x4)*2 + (j-y4)*2) < hd*2:
            screen[j,i,:] = 255

for i in range(x5-hd, x5+hd):
    for j in range(y5-hd, y5+hd):
        if ((i-x5)*2 + (j-y5)*2) < hd*2:
            screen[j,i,:] = 255

for i in range(x6-hd, x6+hd):
    for j in range(y6-hd, y6+hd):
        if ((i-x6)*2 + (j-y6)*2) < hd*2:
            screen[j,i,:] = 255

#Mewarnai isi
# screen[y_min:y_max, x_min:x_max, 0] = 255
# screen[y_min:y_max, x_min:x_max, 1] = 255

plt.figure()
plt.imshow(screen)
plt.show()