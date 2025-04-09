import cv2
import numpy as np
import mediapipe as mp 

# Clase para el detector de manos
class HandDetector:
    def __init__(self, screen_width: int, screen_height: int):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_hands_connections = mp.solutions.hands.HAND_CONNECTIONS
        self.cap = cv2.VideoCapture(0)
        self.camera_width, self.camera_height = screen_width, screen_height

    def detect_hand(self) -> tuple[float | None, float | None, bool, np.ndarray, list | None]:
        ret, frame = self.cap.read()
        if not ret:
            return None, None, False, None, None

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (self.camera_width, self.camera_height))
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb_frame)

        index_x = None
        index_y = None
        is_closed = False
        landmarks = None

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                index_finger = hand_landmarks.landmark[8]  # Dedo índice
                index_x = hand_landmarks.landmark[8].x
                index_y = hand_landmarks.landmark[8].y
                thumb_tip = hand_landmarks.landmark[4].y
                pinky_tip = hand_landmarks.landmark[20].y
                is_closed = abs(thumb_tip - pinky_tip) < 0.05
                landmarks = hand_landmarks.landmark
                self.mp_draw.draw_landmarks(rgb_frame, hand_landmarks, self.mp_hands_connections)

        rgb_frame = cv2.flip(rgb_frame, 1)
        rgb_frame = cv2.resize(rgb_frame, (self.camera_width, self.camera_height))
        rgb_frame = np.rot90(rgb_frame)
        return index_x, index_y, is_closed, rgb_frame, landmarks

    def release(self):
        self.cap.release() 


