import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(1)   ###İSTERSEN 2.mp4 isimli videoyu kullanarak video üzerinde de tanıma yapabilirsin

cizme=[i for i in range(27,36)]

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #68 noktalı veriset
color_list=[(255,0,0),(255, 153, 102),(255, 102, 255),(0, 255, 0),(255, 102, 102)] #RENKLER
number=0
width = int(cap.get(3))  # float
height = int(cap.get(4)) 
just_dots=False
which_arr=[]

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ndarray = np.full((height, width, 3), 0, dtype=np.uint8)
    
    main_color=color_list[number]
    faces = detector(gray)
    

    
    if just_dots:
        which_arr=ndarray
    else:
        which_arr=frame

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        
        #cv2.rectangle(which_arr, (x1, y1), (x2, y2), (0, 255, 0), 1)
        
        
        ##### YÜZ HATLARINA GÖRE ÇİZGİ ÇİZME EYLEMİ BURADA GERÇEKLEŞECEK
        
        
        landmarks = predictor(gray, face)
        
        ### BURUN KISMI ###
        
        start_point = (landmarks.part(27).x, landmarks.part(27).y) 
        end_point = (landmarks.part(30).x, landmarks.part(30).y) 
  
        cv2.line(which_arr, start_point, end_point, (0, 255, 0), 1) 

        start_point = (landmarks.part(27).x, landmarks.part(27).y) 
        end_point = (landmarks.part(31).x, landmarks.part(31).y) 
        
        cv2.line(which_arr, start_point, end_point, (0, 255, 0), 1) 

        
        start_point = (landmarks.part(27).x, landmarks.part(27).y) 
        end_point = (landmarks.part(35).x, landmarks.part(35).y) 
  
        cv2.line(which_arr, start_point, end_point, (0, 255, 0), 1) 
        
        start_point = (landmarks.part(31).x, landmarks.part(31).y) 
        end_point = (landmarks.part(33).x, landmarks.part(33).y) 
  
        cv2.line(which_arr, start_point, end_point, (0, 255, 0), 1)
        
        start_point = (landmarks.part(33).x, landmarks.part(33).y) 
        end_point = (landmarks.part(35).x, landmarks.part(35).y) 
  
        cv2.line(which_arr, start_point, end_point, (0, 255, 0), 1)
        
        ### BURUN KISMI ###
        
        
        

        
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            
            if n in cizme:
                pass
            else:
                
                cv2.circle(which_arr, (x, y), 1, main_color, -1)
                
  
    cv2.imshow('Gelecege Hosgeldin Evlat!', which_arr)

    key = cv2.waitKey(1)
   
    if key==ord("a"):
        if just_dots:
            just_dots=False
        else:
            just_dots=True
    
    if key == 27:

        break
    if key == ord(" "):
        if number==4:
            number=0
        else:
            number+=1
            