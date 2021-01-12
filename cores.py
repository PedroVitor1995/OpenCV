import cv2

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

def image(imagem):
    separarCanais(imagem)

if __name__ == '__main__':
    image('imagem.jpg')