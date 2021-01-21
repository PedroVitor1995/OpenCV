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

def image(imagem):
    original(imagem)


if __name__ == '__main__':
    image('imagem.jpg')