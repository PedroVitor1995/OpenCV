import cv2
import numpy
from matplotlib import pyplot
import math

def original(imagem):
    img = cv2.imread(imagem)
    cv2.imshow("Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cinza(imagem):
    img = cv2.imread(imagem)

    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    cv2.imshow("Cinza", imgGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##  Segmentar as partes da estrutura da proteína anexa
def segmentar(imagem):
    img = cv2.imread(imagem)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blur = cv2.medianBlur(hsv, 9)

    cv2.imshow("Segmentar", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


##  Técnicas Sistemas de Cores
def hsv(imagem):
    img = cv2.imread(imagem)

    imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    cv2.imshow("HSV", imgHSV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def separarCanais(imagem):
    img = cv2.imread(imagem)

    channels = cv2.split(img)

    cv2.imshow("Blue", channels[0])
    cv2.imshow("Green", channels[1])
    cv2.imshow("Red", channels[2])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##  Técnicas de Filtros
def filtro_media(imagem):
    img = cv2.imread(imagem)

    blur = cv2.blur(img,(5,5))

    pyplot.subplot(121),pyplot.imshow(img),pyplot.title("Original")
    pyplot.xticks([]),pyplot.yticks([])
    pyplot.subplot(122),pyplot.imshow(blur),pyplot.title("Blurred")
    pyplot.xticks([]),pyplot.yticks([])
    pyplot.show()

def filtro_mediana(imagem):
    img = cv2.imread(imagem)

    median = cv2.medianBlur(img, 5)

    pyplot.subplot(121), pyplot.imshow(img), pyplot.title("Original")
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.subplot(122), pyplot.imshow(median), pyplot.title("Blurred")
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

def filtro_gaussiano(imagem):
    img = cv2.imread(imagem)

    blur = cv2.GaussianBlur(img, (5, 5), 0)

    pyplot.subplot(121),pyplot.imshow(img),pyplot.title("Original")
    pyplot.xticks([]),pyplot.yticks([])
    pyplot.subplot(122),pyplot.imshow(blur),pyplot.title("Blurred")
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

##  Técnicas de Realce
def negativo(imagem):
    img = cv2.imread(imagem)

    for y in range(0,img.shape[0]):
        for x in range(0,img.shape[1]):
            img[y,x] = 255 - img[y,x]

    cv2.imshow("Negativo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def normalizacao(imagem):
    img = cv2.imread(imagem)

    a = 0
    b = 255
    c = 100
    d = 170
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            img[y, x] = (img[y, x] - a) * ((d - c) / (b - a)) + c

    cv2.imshow("Normalizacao", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def realce_gama(imagem):
    img = cv2.imread(imagem,0)

    c = 5
    gama = 0.7
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            img[y,x] = c * img[y,x] ** gama

    cv2.imshow("Gama", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def logaritmico(imagem):
    img = cv2.imread(imagem,0)

    G = 50

    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            img[y,x] = G * math.log10(img[y,x] + 1)

    cv2.imshow("Logaritmico", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


##  Imagem
def image(imagem):
    segmentar(imagem)

if __name__ == '__main__':
    image('Alcohol-Dehydrogenase.png')