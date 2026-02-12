import mediapipe as mp
import numpy as np
import time

mp_face = mp.solutions.face_mesh


class BlinkDetector:
    def __init__(self):
        self.face_mesh = mp_face.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # EAR thresholds
        self.EAR_THRESHOLD = 0.20
        self.EYE_CLOSED_TIME = 2.5  # seconds → prolonged closure

        # State
        self.eye_closed_since = None
        self.blink_count = 0
        self.prev_eye_closed = False

        # MediaPipe eye landmarks
        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    def _eye_aspect_ratio(self, landmarks, eye_indices, w, h):
        p = [(landmarks[i].x * w, landmarks[i].y * h) for i in eye_indices]

        vertical_1 = np.linalg.norm(np.array(p[1]) - np.array(p[5]))
        vertical_2 = np.linalg.norm(np.array(p[2]) - np.array(p[4]))
        horizontal = np.linalg.norm(np.array(p[0]) - np.array(p[3]))

        if horizontal == 0:
            return 0.0

        return (vertical_1 + vertical_2) / (2.0 * horizontal)

    def update(self, frame):
        h, w, _ = frame.shape
        rgb = frame[:, :, ::-1]
        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            self.eye_closed_since = None
            return {
                "blink": False,
                "eye_closed": False,
                "prolonged_eye_closure": False,
                "blink_count": self.blink_count
            }

        landmarks = result.multi_face_landmarks[0].landmark

        left_ear = self._eye_aspect_ratio(landmarks, self.LEFT_EYE, w, h)
        right_ear = self._eye_aspect_ratio(landmarks, self.RIGHT_EYE, w, h)

        ear = (left_ear + right_ear) / 2.0
        eye_closed = ear < self.EAR_THRESHOLD
        now = time.time()

        prolonged = False
        blink = False

        if eye_closed:
            if self.eye_closed_since is None:
                self.eye_closed_since = now
        else:
            if self.prev_eye_closed:
                blink = True
                self.blink_count += 1
            self.eye_closed_since = None

        if self.eye_closed_since:
            if now - self.eye_closed_since >= self.EYE_CLOSED_TIME:
                prolonged = True

        self.prev_eye_closed = eye_closed

        return {
            "blink": blink,
            "eye_closed": eye_closed,
            "prolonged_eye_closure": prolonged,
            "blink_count": self.blink_count
        }
