import cv2 # pip install opencv-python 
import mediapipe as mp # pip install mediapipe
import time
import numpy as np #pip install numpy
import math
from comtypes import CLSCTX_ALL # pip install comtypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume # pip install pycaw
import win32api # pip install pywin32

from win32con import * # pip install pywin32
####################################
wCam,hCam=640,480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
####################################

mpHands = mp.solutions.hands
hands=mpHands.Hands()
mpDraw= mp.solutions.drawing_utils

pTime = 0
cTime = 0

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange=volume.GetVolumeRange()

minVol=volRange[0]
maxVol=volRange[1]


sayac=0
while True:
    lmList=[]

    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: 
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
        
            for id, lm in enumerate(handLms.landmark):   
                h, w, c = img.shape
                cpx, cpy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cpx, cpy])
               
                
                if len(lmList)==20:
                    
                
                    x1,y1=lmList[4][1],lmList[4][2]#başparmak x ve y kordinatı
    
                    x2,y2=lmList[8][1],lmList[8][2]#işaret parmağı x ve y kordinatı     
                    x3,y3=lmList[0][1],lmList[0][2]#işaret parmağı x ve y kordinatı     
                    x4,y4=lmList[16][1],lmList[16][2]#işaret parmağı x ve y kordinatı     
                   

                    cv2.circle(img,(x1,y1),5,(255,0,0),cv2.FILLED)#başparmak  pointer'ı
                    cv2.circle(img,(x2,y2),5,(255,0,0),cv2.FILLED)#işaret parmağı pointer'ı
                    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)#başparmak ve işaret parmağı arası çizgi (sesi kontrol eden line)
                    cv2.line(img,(x1,y1),(x4,y4),(0,0,255),2)#başparmak ve işaret parmağı arası çizgi (sesi kontrol eden line)

                
                    mlength=math.hypot(x4-x1,y4-y1)#media çizgisinin uzunluğu
                    vlength=math.hypot(x2-x1,y2-y1)#volume çizgisinin uzunluğu

                    vlength=int(vlength)
                    mlength=int(mlength)

                    if mlength<=60 and sayac ==0:
                        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE,KEYEVENTF_EXTENDEDKEY)
                        sayac+=1
                    if mlength>90:
                        sayac=0


                    vol=np.interp(vlength,[20,200],[minVol,maxVol])

                    volume.SetMasterVolumeLevel(int(vol), None)

#################---- FPS ----#####################
    cTime = time.time()      
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    #kaynak,değer,pozisyon,font,boyut,renk,kalınlık

####################################################
    
    cv2.imshow("Image",img)

    if cv2.waitKey(1)& 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()