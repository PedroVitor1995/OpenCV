import cv2
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

def gama(imagem):
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

def image(imagem):
    logaritmico(imagem)

if __name__ == '__main__':
    image('imagem.jpg')