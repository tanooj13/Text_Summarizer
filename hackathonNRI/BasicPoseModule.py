import cv2
import mediapipe as mp
import math

class PoseDetectorModified():

    def __init__(self, mode=False, complexity=1, smooth_landmarks=True,
                 enable_segmentation=False, smooth_segmentation=True,
                 detectionCon=0.5, trackCon=0.5):
        """
            Initializes a new instance of the PoseDetectorModified class.

            Args:
                mode (bool): Whether to use the upper-body-only pose landmark model or the full-body pose landmark model.
                complexity (int): Complexity of the pose landmark model (must be between 0 and 2).
                smooth_landmarks (bool): Whether to smooth the pose landmarks or not.
                enable_segmentation (bool): Whether to enable person segmentation or not.
                smooth_segmentation (bool): Whether to smooth the person segmentation or not.
                detectionCon (float): Minimum confidence value (between 0 and 1) for the detection to be considered successful.
                trackCon (float): Minimum confidence value (between 0 and 1) for the tracking to be considered successful.
        """

        self.mode = mode
        self.complexity = complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.smooth_landmarks,
                                     self.enable_segmentation, self.smooth_segmentation,
                                     self.detectionCon, self.trackCon)

    def find_pose(self, img, draw=True):
        """
        Finds the pose landmarks and connections in an image or a video frame.

        Args:
            img (numpy.ndarray): The input image or video frame.
            draw (bool): Whether to draw the pose landmarks and connections on the image or not.

        Returns:
            The input image with the pose landmarks and connections drawn on it (if `draw` is True).
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)

        return img

    def find_position(self, img, draw=True):
        """
            Finds the pose landmark positions in an image or a video frame.

            Args:
                img (numpy.ndarray): The input image or video frame.
                draw (bool): Whether to draw the pose landmark positions on the image or not.

            Returns:
                A list containing the landmark ID, X and Y positions for each landmark in the pose.
        """
        lm_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lm_list

    def find_angle(self, img, p1, p2, p3, lm_list, draw=True):
        """
        Calculates the angle between three landmarks.

        Args:
            img (numpy.ndarray): The input image or video frame.
            p1 (int): ID of the first landmark.
            p2 (int): ID of the second landmark (vertex of the angle).
            p3 (int): ID of the third landmark.
            lm_list (list): List of landmarks with their coordinates.
            draw (bool): Whether to draw the angle on the image or not.

        Returns:
            float: The calculated angle in degrees.
        """
        x1, y1 = lm_list[p1][1:]
        x2, y2 = lm_list[p2][1:]
        x3, y3 = lm_list[p3][1:]

        # Calculate the angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        angle = abs(angle)
        if angle > 180:
            angle = 360 - angle

        # Draw the angle on the image
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        return angle

def main():
    detector = PoseDetectorModified()
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, img = cap.read()
        if ret:
            img = detector.find_pose(img)
            lm_list = detector.find_position(img, False)
            if len(lm_list) != 0:
                angle = detector.find_angle(img, 11, 13, 15, lm_list)
                print(angle)
            cv2.imshow('Pose Detection', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
