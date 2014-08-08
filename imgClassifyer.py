import kNN as kNN
import img2txt as img2txt

PATH = './trainingDigits/'
FILE_NAME = '2.jpg'
outFileName = img2txt.img2txt(FILE_NAME,32,32)
inX = kNN.img2vector(outFileName)
print kNN.handwritingClassifyer(inX,PATH)
