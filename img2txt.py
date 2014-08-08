from numpy import *
from PIL import Image as img

#change a pic file to 32*32 pic file and return a 32*32 matrix
def img2matrix(filename,length,height):
    pic = img.open(filename)
    newpic = pic.resize((length,height))
    pixdata = newpic.load()

    returnMatrix = zeros([length,height])

    for y in xrange(newpic.size[1]):
        for x in xrange(newpic.size[0]):
            if pixdata[x,y][0] < 90:
                returnMatrix[y,x] = 1
                pixdata[x,y] = (0, 0, 0, 255)

    for y in xrange(newpic.size[1]):
        for x in xrange(newpic.size[0]):
            if pixdata[x,y][1] < 136:
                returnMatrix[y,x] = 1
                pixdata[x,y] = (0, 0, 0, 255)

    for y in xrange(newpic.size[1]):
        for x in xrange(newpic.size[0]):
            if pixdata[x,y][2] > 0:
                returnMatrix[y,x] = 0
                pixdata[x,y] = (255, 255, 255, 255)


    return returnMatrix


def matrix2file(matrix, filename):
    fr = open(filename,'w+')
    for x in range(matrix.shape[0]):
        tmpStr = ""
        for y in range(matrix.shape[1]):
            tmpStr = tmpStr + "%s" % (int(matrix[x][y]))
        fr.write(tmpStr+"\n")

    fr.close()

#change an img to length*height txt
def img2txt(filename, length, height):
    matrix = img2matrix(filename, length, height)
    txtName = filename.split('.')[0] + ".txt"
    matrix2file(matrix, txtName)
    return txtName