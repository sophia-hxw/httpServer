import base64
import cv2

def base64_to_image(base64_code):
    import numpy as np

    img_data = base64.b64decode(base64_code)
    img_array = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
    return img

def image_to_base64(image_np):

    image = cv2.imencode('.jpg',image_np)[1]
    image_code = str(base64.b64encode(image))[2:-1]

    return image_code