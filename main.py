import cv2

from detectors.face_gaze import FaceGazeDetector
from detectors.phone_detector import PhoneDetector
from logic.focus_score import FocusScore
from logic.distraction_state import DistractionState
from utils.drawing import draw_ui
from detectors.blink_detector import BlinkDetector

# -------------------- Setup --------------------
cap = cv2.VideoCapture(0)
window_name = "Real-Time Distraction Detector"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(
    window_name,
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_NORMAL
)


face_gaze = FaceGazeDetector()
phone_detector = PhoneDetector()
score_tracker = FocusScore()
distraction_state = DistractionState()
blink_detector = BlinkDetector()

# -------------------- Main Loop --------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect signals
    gaze = face_gaze.get_gaze_status(frame)
    phone_detected = phone_detector.phone_present(frame)
    face_present = gaze != "NO_FACE"

    # Update distraction state (time-based)
    state, reason = distraction_state.update(
    gaze=gaze,
    phone=phone_detected,
    face_present=face_present
    )

    # Update focus score
    score = score_tracker.update(
        gaze=gaze,
        phone=phone_detected,
        face_present=face_present
    )

    blink_data = blink_detector.update(frame)

    # Draw UI
    draw_ui(frame, state, score, gaze, phone_detected, reason)

    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------- Cleanup --------------------
cap.release()
cv2.destroyAllWindows()
