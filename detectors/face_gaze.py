import cv2
import mediapipe as mp

mp_face = mp.solutions.face_mesh


class FaceGazeDetector:
    def __init__(self):
        self.face_mesh = mp_face.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # Natural movement tolerance
        self.HORIZONTAL_TOL = 0.20
        self.VERTICAL_TOL = 0.18

    def get_gaze_status(self, frame):
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            return "NO_FACE"

        lm = result.multi_face_landmarks[0].landmark

        # Key points
        nose = lm[1]
        left_eye = lm[33]
        right_eye = lm[263]
        chin = lm[152]
        forehead = lm[10]

        # Pixel positions
        nose_x, nose_y = nose.x * w, nose.y * h
        eye_cx = (left_eye.x + right_eye.x) / 2 * w
        eye_cy = (left_eye.y + right_eye.y) / 2 * h

        face_width = abs((right_eye.x - left_eye.x) * w)
        face_height = abs((chin.y - forehead.y) * h)

        if face_width == 0 or face_height == 0:
            return "UNKNOWN"

        # Normalized offsets
        dx = (nose_x - eye_cx) / face_width
        dy = (nose_y - eye_cy) / face_height

        # Horizontal
        if abs(dx) <= self.HORIZONTAL_TOL and abs(dy) <= self.VERTICAL_TOL:
            return "LOOKING_FORWARD"

        if abs(dx) > abs(dy):
            return "LOOKING_RIGHT" if dx > 0 else "LOOKING_LEFT"
        else:
            return "LOOKING_DOWN" if dy > 0 else "LOOKING_UP"
