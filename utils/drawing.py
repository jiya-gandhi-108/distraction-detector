import cv2

def draw_ui(frame, state, score, gaze, phone, reason):
    cv2.putText(frame, f"State: {state}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.putText(frame, f"Focus Score: {score}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

    cv2.putText(frame, f"Gaze: {gaze}", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.putText(frame, f"Phone Detected: {phone}", (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.putText(frame, f"Blinks: {blink_data['blink_count']}",
            (20, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    if blink_data["prolonged_eye_closure"]:
    cv2.putText(frame, "Eyes Closed Too Long!",
                (20, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    if reason:
        cv2.putText(frame, f"Distraction Reason: {reason}", (20, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2)
