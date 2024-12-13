import cv2
import numpy as np
import BasicPoseModule as pm_modified
import time

cap = cv2.VideoCapture("C:\\Users\\megal\\Downloads\\biceps (1).mp4")
pose_detector = pm_modified.PoseDetectorModified()
counter = 0
movement_dir = 0
pTime = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.resize(frame, (1280, 720))
    frame = pose_detector.find_pose(frame, False)
    landmarks_list = pose_detector.find_position(frame, False)

    if len(landmarks_list) != 0:
        elbow_angle = pose_detector.find_angle(frame, 11, 13, 15, landmarks_list)

        progress_percentage = np.interp(elbow_angle, (50, 160), (0, 100))
        progress_bar = np.interp(elbow_angle, (50, 160), (650, 100))

        color = (255, 0, 255)
        if progress_percentage == 100:
            color = (0, 255, 0)
            if movement_dir == 0:
                counter += 0.5
                movement_dir = 1
        if progress_percentage == 0:
            color = (0, 0, 255)
            if movement_dir == 1:
                counter += 0.5
                movement_dir = 0

        # Draw Progress Bar
        cv2.rectangle(frame, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(frame, (1100, int(progress_bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(frame, f'{int(progress_percentage)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

        # Draw Counter
        cv2.rectangle(frame, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, str(int(counter)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 30)

    # Display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, f'FPS: {int(fps)}', (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Bicep Curls Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
