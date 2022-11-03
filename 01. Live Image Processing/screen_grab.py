import cv2
import numpy as np
from PIL import ImageGrab
import time

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2 = 300)
    vertices = np.array([[10, 500], [10, 300], [300,200], [500, 200], [800, 300], [800, 500]])
    processed_img = roi(processed_img, [vertices])
    return processed_img

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def main():
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
        new_screen =   process_img(screen)
        print('Loop took {} seconds'.format(time.time()- last_time))
        last_time = time.time()
        cv2.imshow("window", new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()
