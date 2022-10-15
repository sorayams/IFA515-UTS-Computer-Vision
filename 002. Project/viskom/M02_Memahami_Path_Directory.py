import matplotlib.pyplot as plt
from skimage.io import imread, imsave
import warnings
warnings.filterwarnings("ignore")


#USER ENTRY
path = "/Users/sorayams/PycharmProjects/viskom/"
file = "punthuk_setumbu"

#READ A FILE (IMAGE) FROM A DIRECTORY
pic = imread(path + file + ".jpeg")

#SHOW THE IMAGE
plt.figure(1)
plt.imshow(pic)
plt.show()
print(path + file + "_01" + ".jpeg")

# Cara 1
for i in range(10):
    imsave(path + file + str(i+1) + ".jpeg", pic)

# Cara 2
i = 0
while i < 10:
    i = i + 1
    imsave(path + file + str(i) + "a.jpeg", pic)

#SAVE IMAGE BACK TO PATH
# imsave(path + file + "_01" + ".jpeg", pic)