from PIL import Image
import numpy as np

img1 = Image.open("D:\Video Recourses/77-776627_and-this-ladies-and-gentlemen-anime-girl-shrug.png")
img2 = Image.open("D:\Video Recourses/kdawallpaper.jpg")

img1_array = np.array(img1)
img2_array = np.array(img2)

imgg = np.hstack([img1_array, img2_array])

finalimg = Image.fromarray(imgg)

finalimg.save("D:\Video Recourses/referance images")
print("Image saved")