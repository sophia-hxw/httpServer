# ClientServer
simple c-s structure in python for cver(means using base64 to transport images)

## server
* get a json string from clients
* translate the base64 string to a matrix using cv2
* response clients a json string with your results in "feature"

## client
* a image in your computer translate to base64 string
* post a request using json string made by your base64 string
* get the response from your server