# Program Untuk Persegi Panjang

print("\033c")
import numpy as np
import matplotlib.pyplot as plt

# Set the screen size
col = int(1920); row = int(1080)

# Set the number of points (4 for rectangle)
# Then assign coordinates for each points
no_of_points = 4
# [dummy, x1, x2, x3, x4, x1]
# [dummy, y1, y2, y3, y4, y1]
# Value of the last position is the same as x1
xn = [0, 1300, 700, 700, 1300, 1300]
yn = [0, 300, 300, 700, 700, 300]

# Setting up point diameter & line width
pd = int(3); lw = int(10)

# Calculate half point diameter & line width
hd = int(pd/2); hw = int(lw/2)

# Creating black screen as the background
screen = np.zeros(shape=(row, col, 3), dtype=np.uint8)

# Drawing the four points white (loop, condition, comparation)
for k in range (1, no_of_points+1):
    x = xn[k]; y = yn [k]
    for i in range(x-hd, x+hd):
        for j in range(y-hd, y+hd):
            if ( (i-x)**2 + (j-y)**2 ) < hd**2:
                screen[j,i,:]=255

# Creating lines in between points
for k in range (1, no_of_points+1):
    xa = xn[k]; xb = xn[k+1]
    ya = yn[k]; yb = yn[k+1]
    x_min = min(xa,xb); x_max = max(xa,xb)
    y_min = min(ya,yb); y_max = max(ya,yb)
    dy = yb-ya; dx = xb-xa
    if abs(dy) <= abs(dx):
        print("Now creating the line using 'my'...")
        my = dy/dx
        for i in range(x_min, x_max):
            j = int(my * (i-xa) + ya)   # Finding y using x values
            x = i
            y = j
            print('x,y=', x, ',', y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw): # Creating red circles surrounding (x,y)
                    if ( (i-x)**2 + (j-y)**2 ) < hw**2:
                        screen[j,i,0] = 255

    if abs(dx) < abs(dy):
        print("Now creating the line using 'mx'...")
        mx = dx/dy
        for j in range(y_min, y_max):
            i = int(mx * (j-ya) + xa)   # Finding x using y value
            x = i
            y = j
            print('x,y =', x, ',', y)
            for i in range(x-hw, x+hw): # Creating red circles surrounding (x,y)
                for j in range(y-hw, y+hw):
                    if ( (i-x)**2 + (j-y)**2 ) < hw **2:
                        screen[j,i,0] = 255

# Drawing the fill violet (red + blue)
x_min = min(xn[1:no_of_points]); x_max = max(xn[1:no_of_points])
y_min = min(yn[1:no_of_points]); y_max = max(yn[1:no_of_points])
screen[y_min+hw:y_max-hw, x_min+hw:x_max-hw, 0] = 84
screen[y_min+hw:y_max-hw, x_min+hw:x_max-hw, 0] = 88
screen[y_min+hw:y_max-hw, x_min+hw:x_max-hw, 2] = 167


plt.figure()
plt.imshow(screen)
plt.show()