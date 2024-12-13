import cv2
import numpy as np
import BasicPoseModule as pm

video_capture = cv2.VideoCapture("C:\\Users\\megal\\Downloads\\pullups (1).mp4")  # Initialize video capture using the webcam
frame_delay = int(1000 / video_capture.get(cv2.CAP_PROP_FPS))
pose_detector = pm.PoseDetectorModified()
counter = 0
movement_dir = 0
correct_form = 0
exercise_feedback = "Fix Form"

while video_capture.isOpened():
    success, frame = video_capture.read()
    video_width = video_capture.get(3)
    video_height = video_capture.get(4)

    frame = pose_detector.find_pose(frame, False)
    landmarks_list = pose_detector.find_position(frame, False)

    if len(landmarks_list) != 0:
        elbow_angle = pose_detector.find_angle(frame, 11, 13, 15, landmarks_list)
        shoulder_angle = pose_detector.find_angle(frame, 11, 23, 25, landmarks_list)

        progress_percentage = np.interp(elbow_angle, (70, 160), (0, 100))
        progress_bar = np.interp(elbow_angle, (70, 160), (380, 50))

        if elbow_angle > 70 and shoulder_angle < 160:
            correct_form = 1

        if correct_form == 1:
            if progress_percentage == 0:
                if elbow_angle <= 70 and shoulder_angle < 160:
                    exercise_feedback = "Up"
                    if movement_dir == 0:
                        counter += 0.5
                        movement_dir = 1
                else:
                    exercise_feedback = "Fix Form"

            if progress_percentage == 100:
                if elbow_angle > 160 and shoulder_angle < 160:
                    exercise_feedback = "Down"
                    if movement_dir == 1:
                        counter += 0.5
                        movement_dir = 0
                else:
                    exercise_feedback = "Fix Form"

        if correct_form == 1:
            cv2.rectangle(frame, (580, 50), (600, 380), (0, 255, 0), 3)
            cv2.rectangle(frame, (580, int(progress_bar)), (600, 380), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, f'{int(progress_percentage)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        cv2.rectangle(frame, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, str(int(counter)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

        cv2.rectangle(frame, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText(frame, exercise_feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cv2.imshow('Pull-Up Counter', frame)
    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):  # Break the loop if 'q' is pressed
        break

video_capture.release()
cv2.destroyAllWindows()
