import math
import time


class GestureEngine:

    def __init__(self):

        # -----------------------------
        # Settings
        # -----------------------------

        self.click_distance = 38
        self.drag_hold = 0.25

        # -----------------------------
        # Click
        # -----------------------------

        self.pinching = False
        self.pinch_start = 0

        # -----------------------------
        # Drag
        # -----------------------------

        self.dragging = False
        self.drag_started = False

        # -----------------------------
        # Double Click
        # -----------------------------

        self.double_active = False

    # =====================================
    # Distance
    # =====================================

    def distance(self, p1, p2):

        return math.hypot(

            p1["x"] - p2["x"],

            p1["y"] - p2["y"]

        )

    # =====================================
    # Main Brain
    # =====================================

    def process(self, hand, is_double):

        action = {

            "left_click": False,

            "double_click": False,

            "drag_start": False,

            "drag_end": False

        }

        now = time.time()

        thumb = hand[4]
        index = hand[8]

        pinch = self.distance(thumb, index)

        # =====================================
        # ✌ DOUBLE CLICK
        # =====================================

        if is_double:

            if not self.double_active:

                action["double_click"] = True

                self.double_active = True

            return action

        else:

            self.double_active = False

        # =====================================
        # 👌 CLICK + 🤏 DRAG
        # =====================================

        if pinch < self.click_distance:

            if not self.pinching:

                self.pinching = True

                self.pinch_start = now

                action["left_click"] = True

            else:

                if (

                    not self.drag_started

                    and

                    now - self.pinch_start >= self.drag_hold

                ):

                    self.drag_started = True

                    self.dragging = True

                    action["drag_start"] = True

        else:

            self.pinching = False

            self.pinch_start = 0

            self.drag_started = False

            if self.dragging:

                self.dragging = False

                action["drag_end"] = True

        return action