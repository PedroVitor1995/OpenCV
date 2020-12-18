import cv2
import numpy

def translacao(imagem):
    img = cv2.imread(imagem,0)
    rows,cols = img.shape
    M = numpy.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow("Translacao", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def escala(imagem):
    img = cv2.imread(imagem)
    res = cv2.resize(img,None,fx=2,fy=2, interpolation=cv2.INTER_CUBIC)

    height,width = img.shape[:2]
    res = cv2.resize(img,(2*width, 2* height),interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Escala", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotacao(imagem):
    img = cv2.imread(imagem,0)
    rows, cols = img.shape

    M = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))

    cv2.imshow("Rotacao", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def espelhamento(imagem):
    img = cv2.imread(imagem)

    horizontal_img = img.copy()
    vertical_img = img.copy()
    both_img = img.copy()

    cv2.imshow("Original",img)
    cv2.imshow("Horizontal", horizontal_img)
    cv2.imshow("Vertical", vertical_img)
    cv2.imshow("Both", both_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def image(imagem):
    espelhamento(imagem)

if __name__ == '__main__':
    image('imagem.jpg')