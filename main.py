import cv2

def image(imagem):
    img = cv2.imread(imagem)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image('imagem.jpg')

