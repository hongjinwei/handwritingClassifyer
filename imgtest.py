from PIL import  Image as img
from numpy import *
im = img.open('4.jpg')
#print im.size
#im.show()

newpic = im.resize((32,32))
#newpic.show()
matrix = zeros([32,32])

pixdata = newpic.load()
for y in xrange(newpic.size[1]):
    for x in xrange(newpic.size[0]):
        if pixdata[x,y][0] < 90:
            matrix[x,y] = 1
            pixdata[x,y] = (0, 0, 0, 255)

for y in xrange(newpic.size[1]):
    for x in xrange(newpic.size[0]):
        if pixdata[x,y][1] < 136:
            matrix[x,y] = 1
            pixdata[x,y] = (0, 0, 0, 255)

for y in xrange(newpic.size[1]):
    for x in xrange(newpic.size[0]):
        if pixdata[x,y][2] > 0:
            matrix[x,y] = 0
            pixdata[x,y] = (255, 255, 255, 255)

newpic.save('4_after.jpg',"JPEG")
print matrix
new = img.open('4_after.jpg')
new.show()
