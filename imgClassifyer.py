from lib import kNN as kNN
from lib import img2txt as img2txt

PATH = './trainingDigits/'
FILE_PATH = './pic/'
FILE_NAME = '2.jpg'
outFileName = img2txt.img2txt(FILE_PATH+FILE_NAME,32,32)
inX = kNN.img2vector(outFileName)
print kNN.handwritingClassifyer(inX,PATH)
