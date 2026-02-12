import time

class DistractionLogic:
    def __init__(self):
        self.last_focus_time = time.time()
        self.state = "FOCUSED"

    def update(self, gaze, phone):
        now = time.time()

        distracted = False

        if gaze != "LOOKING_FORWARD" or phone:
            distracted = True

        if distracted:
            elapsed = now - self.last_focus_time
        else:
            self.last_focus_time = now
            self.state = "FOCUSED"
            return self.state

        if elapsed > 7:
            self.state = "HIGHLY_DISTRACTED"
        elif elapsed > 3:
            self.state = "DISTRACTED"
        else:
            self.state = "BRIEFLY_DISTRACTED"

        return self.state
