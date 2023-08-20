import cv2 as cv
import mediapipe as mp

capture = cv.VideoCapture(0)

facmesh = mp.solutions.face_mesh
face = facmesh.FaceMesh(static_image_mode=True, min_tracking_confidence=0.6, min_detection_confidence=0.6)
draw = mp.solutions.drawing_utils

if not capture.isOpened():  
    
    raise IOError("Cannot open webcam")

else:    
    while True:
        
        ret, frame = capture.read()
        
        if not ret:
            print("We Facing Some Errors")
        
        else:
            frame = cv.resize(frame, (550, 550))
            frame = cv.flip(frame, 1)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            op = face.process(frame)
            
            if op.multi_face_landmarks:
                for i in op.multi_face_landmarks:
                    print(i.landmark[0].y*480)
                    draw.draw_landmarks(frame,i,facmesh.FACEMESH_CONTOURS,landmark_drawing_spec=draw.DrawingSpec(color=(0,255,255)))

            cv.imshow("Frame", frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                capture.release()
                cv.destroyAllWindows()
                break

