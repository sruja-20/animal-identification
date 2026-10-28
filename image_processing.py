import cv2

def convert_image_greyscale(image_path):
    print(image_path)
    image = cv2.imread(image_path)
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)