import cv2
from matplotlib import pyplot

def original(imagem):
    img = cv2.imread(imagem)
    cv2.imshow("Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def image(imagem):
    original(imagem)

if __name__ == '__main__':
    image('Alcohol-Dehydrogenase.png')