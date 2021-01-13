import cv2
from matplotlib import pyplot

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


def image(imagem):
    filtro_gaussiano(imagem)

if __name__ == '__main__':
    image('imagem.jpg')