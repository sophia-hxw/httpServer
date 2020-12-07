
def test_flask_cs():
    import cv2
    from test.http_client import send_request
    from baseimg.img_b64 import image_to_base64

    img_pth = "data/img/boniu.jpg"
    img = cv2.imread(img_pth)
    data_bytes = image_to_base64(img)
    
    send_request(data_bytes)

if __name__ == "__main__":
    test_flask_cs()