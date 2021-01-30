import cv2,os
from os import path as pt

def TakeImages():        
    Id=1
    name=str(input('Enter name of class = '))
    path = os.getcwd()
    path = path.replace("\\",'/')
    path = path + "/images"+ '/' + name

    
    try:
        if not pt.exists(path):
            os.mkdir(path)
            print ("Successfully created the directory %s " % path)

        files_already = list(os.listdir(path))
        #print(files_already)
        if len(files_already)==0:
            start_number = 1
        else:
            a = int(files_already[-1].split('.')[0])
            start_number = a+1
        to_take = 100
        end_number = start_number+to_take
        
        cam = cv2.VideoCapture(0)
        #cam = cv2.VideoCapture('video.mp4')
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=start_number
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.35, 5)
            for (x,y,w,h) in faces:
                       
                #incrementing sample number 
                
                #saving the captured face in the dataset folder TrainingImage
                #cv2.imwrite("images" +"\" +name + "\" +str(sampleNum)".jpg", img[y:y+h,x:x+w])
                filename = "images/{}/{}.jpg".format(name,str(sampleNum))
                cv2.imwrite(filename, img[y:y+h,x:x+w])
                print(filename)
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
                #cv2.imwrite("images\" +name + "\" +str(sampleNum)".jpg, img[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
                sampleNum=sampleNum+1
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>end_number:
                pass
                #break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for : "+ name
            
        
    except OSError:
        print ("failed Creation of the directory %s " % path)        
    
TakeImages()
