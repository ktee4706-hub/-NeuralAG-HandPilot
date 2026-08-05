import ctypes
import time


# Windows API

user32 = ctypes.windll.user32

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_WHEEL = 0x0800


class WindowsMouse:

    def __init__(self):

        self.screen_width = user32.GetSystemMetrics(0)
        self.screen_height = user32.GetSystemMetrics(1)

        self.previous_x = 0
        self.previous_y = 0

        self.smoothing = 5

        self.dragging = False

    # ==========================================
    # Move Cursor
    # ==========================================

    def move(self, x, y, frame_width, frame_height):

        target_x = int(
            (x / frame_width) * self.screen_width
        )

        target_y = int(
            (y / frame_height) * self.screen_height
        )

        smooth_x = self.previous_x + (
            target_x - self.previous_x
        ) / self.smoothing

        smooth_y = self.previous_y + (
            target_y - self.previous_y
        ) / self.smoothing

        user32.SetCursorPos(
            int(smooth_x),
            int(smooth_y)
        )

        self.previous_x = smooth_x
        self.previous_y = smooth_y

    # ==========================================
    # Left Click
    # ==========================================

    def left_click(self):

        user32.mouse_event(
            MOUSEEVENTF_LEFTDOWN,
            0,
            0,
            0,
            0
        )

        time.sleep(0.01)

        user32.mouse_event(
            MOUSEEVENTF_LEFTUP,
            0,
            0,
            0,
            0
        )

    # ==========================================
    # Double Click
    # ==========================================

    def double_click(self):

        self.left_click()

        time.sleep(0.03)

        self.left_click()

    # ==========================================
    # Drag Start
    # ==========================================

    def left_down(self):

        if not self.dragging:

            user32.mouse_event(
                MOUSEEVENTF_LEFTDOWN,
                0,
                0,
                0,
                0
            )

            self.dragging = True

    # ==========================================
    # Drag End
    # ==========================================

    def left_up(self):

        if self.dragging:

            user32.mouse_event(
                MOUSEEVENTF_LEFTUP,
                0,
                0,
                0,
                0
            )

            self.dragging = False

    # ==========================================
    # Right Click
    # ==========================================

    def right_click(self):

        user32.mouse_event(
            MOUSEEVENTF_RIGHTDOWN,
            0,
            0,
            0,
            0
        )

        time.sleep(0.01)

        user32.mouse_event(
            MOUSEEVENTF_RIGHTUP,
            0,
            0,
            0,
            0
        )

    # ==========================================
    # Scroll
    # ==========================================

    def scroll(self, amount):

        user32.mouse_event(
            MOUSEEVENTF_WHEEL,
            0,
            0,
            amount,
            0
        )