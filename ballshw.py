
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops
from skimage import color

def get_colors(elements):
    c = {"red" : 0, "orange": 0, "yellow": 0,"lime": 0,"green": 0,"cyan": 0,"blue": 0,"indigo": 0,"purple": 0,"pink": 0,"fuchsia": 0,"crimson": 0}
    
    for elem in elements:

        if (0 <= elem < 30):
            c['red'] += 1
        if (30 <= elem < 60):
            c['orange'] += 1
        if (60 <= elem < 90):
            c['yellow'] += 1
        if (90 <= elem < 120):
            c['lime'] += 1
        if (120 <= elem < 150):
            c['green'] += 1
        if (150 <= elem < 180):
            c['cyan'] += 1
        if (180 <= elem < 210):
            c['blue'] += 1
        if (210 <= elem < 240):
            c['indigo'] += 1
        if (240 <= elem < 270):
            c['purple'] += 1
        if (270 <= elem < 300):
            c['pink'] += 1
        if (300 <= elem < 330):
            c['fuchsia'] += 1
        if (330 <= elem <= 360):
            c['crimson'] += 1
        
    print(c)


image = plt.imread("C:\\images\\balls_and_rects.png")
binary = image.copy()[:, :, 0]
binary[binary > 0] = 1

image = color.rgb2hsv(image)[:, :, 0] * 360

labeled = label(binary)
balls, rects = [], []
print("Amount of figures:", np.max(labeled))

for region in regionprops(labeled):
    val = np.max(image[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]])

    if region.area == (region.image.shape[0] * region.image.shape[1]):
        rects.append(val)
    else:
        balls.append(val)

print("Balls:", len(balls))
get_colors(balls)

print("Rects:", len(rects))
get_colors(rects)

plt.figure()
plt.imshow(image)
plt.show()