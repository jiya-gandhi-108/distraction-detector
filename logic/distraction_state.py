import time
from collections import deque, Counter


class DistractionState:
    def __init__(self):
        # Time thresholds (seconds)
        self.BRIEF_THRESHOLD = 2
        self.HIGH_THRESHOLD = 10

        # Temporal smoothing
        self.BUFFER_SIZE = 15
        self.signal_buffer = deque(maxlen=self.BUFFER_SIZE)

        # State tracking
        self.distracted_since = None
        self.state = "FOCUSED"
        self.reason = None

    def _get_reason(self, gaze, phone, face_present, blink_data):
    if not face_present:
        return "NO_FACE"
    if blink_data["prolonged_eye_closure"]:
        return "EYES_CLOSED"
    if phone:
        return "PHONE"
    if gaze != "LOOKING_FORWARD":
        return "LOOKING_AWAY"
    return "FOCUSED"


    def update(self, gaze, phone, face_present):
        now = time.time()

        # Step 1: Determine current frame reason
        reason = self._get_reason(gaze, phone, face_present)
        self.signal_buffer.append(reason)

        # Step 2: Temporal smoothing (majority vote)
        counts = Counter(self.signal_buffer)
        dominant_reason = counts.most_common(1)[0][0]

        # Step 3: Apply grace periods
        if dominant_reason == "FOCUSED":
            self.state = "FOCUSED"
            self.reason = None
            self.distracted_since = None
            return self.state, self.reason

        # Distraction ongoing
        if self.distracted_since is None:
            self.distracted_since = now

        duration = now - self.distracted_since

        if duration >= self.HIGH_THRESHOLD:
            self.state = "HIGHLY_DISTRACTED"
        elif duration >= self.BRIEF_THRESHOLD:
            self.state = "BRIEFLY_DISTRACTED"
        else:
            # Still within grace period
            self.state = "FOCUSED"
            self.reason = None
            return self.state, self.reason

        self.reason = dominant_reason
        return self.state, self.reason
