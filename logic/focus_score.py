class FocusScore:
    def __init__(self):
        self.score = 100

    def update(self, gaze, phone, face_present):
        """
        Focus score logic:
        - Penalize clear distraction
        - Recover slowly when focused
        """

        if not face_present:
            # Severe penalty
            self.score -= 3

        elif phone:
            self.score -= 5

        elif gaze == "LOOKING_AWAY":
            self.score -= 2

        elif gaze == "LOOKING_FORWARD":
            # Recovery only when clearly focused
            self.score += 1

        # Clamp score
        self.score = max(0, min(100, self.score))
        return self.score
 