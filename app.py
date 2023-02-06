from logging import info 
import cv2
from flask import  Flask, request , render_template
from tqdm.gui import trange 

app= Flask(_name_)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('help.html')
@app.route('/',methods=['POST','GET'])
def show(): 

name2=request.form['vid'] 

 

face_cascade = cv2.CascadeClassifier("C:\\Users\\vaish\\OneDrive\\Documents\\Test\\venv\\Lib\\si te-packages\\cv2\\data\\haarcascade_frontalface_default.xml") 

cap = cv2.VideoCapture(name2) img_array = [] 

f=0 

 

for j in trange(500,desc="Processing",bar_format="{desc}: 

{percentage:3.0f}%"): 

_, img = cap.read() 

gray = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE) faces = face_cascade.detectMultiScale(gray, 1.1, 4) 

 

for (x, y, w, h) in faces: ROI = img[y:y+h, x:x+w] 

blur = cv2.GaussianBlur(ROI, (27,27), 0) img[y:y+h, x:x+w] = blur 

 

height, width, layers = img.shape size = (width,height) 

 

 

img_array.append(img) 

 

cap.release() out = 

cv2.VideoWriter('video_processed.mp4',cv2.VideoWriter_fourcc(*'DIVX'),15,size) 

 

for i in range(len(img_array)): out.write(img_array[i]) 

out.release() 

 

return render_template('index.html',info="Anonymized Video successfully exported to original path") 

 

if name ==' main ': app.run(debug=True) 