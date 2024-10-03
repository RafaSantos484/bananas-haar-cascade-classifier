import os
import cv2
from params import scaleFactor, minNeighbors


def run():
    classifier = cv2.CascadeClassifier('result.xml')
    for filename in os.listdir('test_imgs'):
        img_path = os.path.join('test_imgs', filename)
        img = cv2.imread(img_path)
        result = classifier.detectMultiScale(img, scaleFactor, minNeighbors)
        print(result)
        for x, y, wdt, hght in result:
            cv2.rectangle(img, (x, y), (x + wdt, y + hght), (255, 0, 0), 2)

        cv2.imshow(filename, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
