import cv2

from camera.hand_tracker import HandTracker
from mouse.windows_mouse import WindowsMouse
from brain.gesture_engine import GestureEngine


# ==========================================
# Initialize
# ==========================================

tracker = HandTracker()
mouse = WindowsMouse()
brain = GestureEngine()


# ==========================================
# Camera
# ==========================================

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("=" * 50)
print("KTEE Virtual Mouse")
print("Move + Click + Drag + Double Click")
print("=" * 50)


# ==========================================
# Main Loop
# ==========================================

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    frame = tracker.find_hands(frame)

    hands = tracker.get_landmarks(frame)

    if len(hands) > 0:

        hand = hands[0]

        # ======================================
        # Move Cursor
        # ======================================

        index = hand[8]

        mouse.move(

            index["x"],

            index["y"],

            frame.shape[1],

            frame.shape[0]

        )

        # ======================================
        # Detect Double Click Gesture
        # ======================================

        is_double = tracker.is_double_click(hand)

        # ======================================
        # Gesture Engine
        # ======================================

        action = brain.process(

            hand,

            is_double

        )

        # ======================================
        # Left Click
        # ======================================

        if action["left_click"]:

            mouse.left_click()

        # ======================================
        # Double Click
        # ======================================

        if action["double_click"]:

            mouse.double_click()

        # ======================================
        # Drag Start
        # ======================================

        if action["drag_start"]:

            mouse.left_down()

        # ======================================
        # Drag End
        # ======================================

        if action["drag_end"]:

            mouse.left_up()

        # ======================================
        # Debug Text
        # ======================================

        text = "MOVE"

        if mouse.dragging:

            text = "DRAG"

        elif action["double_click"]:

            text = "DOUBLE CLICK"

        elif action["left_click"]:

            text = "CLICK"

        elif is_double:

            text = "DOUBLE CLICK"

        cv2.putText(

            frame,

            text,

            (20, 40),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0, 255, 0),

            2

        )

    else:

        if mouse.dragging:

            mouse.left_up()

    cv2.imshow(


    "KTEE Virtual Mouse",

    frame
    )

    if cv2.waitKey(1) == 27:

        break


cap.release()

cv2.destroyAllWindows()

from camera.hand_tracker import HandTracker
from mouse.windows_mouse import WindowsMouse
from brain.gesture_engine import GestureEngine


# ==========================================
# Initialize
# ==========================================

tracker = HandTracker()
mouse = WindowsMouse()
brain = GestureEngine()


# ==========================================
# Camera
# ==========================================

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("=" * 50)
print("KTEE Virtual Mouse")
print("Move + Click + Drag + Double Click")
print("=" * 50)


# ==========================================
# Main Loop
# ==========================================

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    frame = tracker.find_hands(frame)

    hands = tracker.get_landmarks(frame)

    if len(hands) > 0:

        hand = hands[0]

        # ======================================
        # Move Cursor
        # ======================================

        index = hand[8]

        mouse.move(

            index["x"],

            index["y"],

            frame.shape[1],

            frame.shape[0]

        )

        # ======================================
        # Detect Double Click Gesture
        # ======================================

        is_double = tracker.is_double_click(hand)

        # ======================================
        # Gesture Engine
        # ======================================

        action = brain.process(

            hand,

            is_double

        )

        # ======================================
        # Left Click
        # ======================================

        if action["left_click"]:

            mouse.left_click()

        # ======================================
        # Double Click
        # ======================================

        if action["double_click"]:

            mouse.double_click()

        # ======================================
        # Drag Start
        # ======================================

        if action["drag_start"]:

            mouse.left_down()

        # ======================================
        # Drag End
        # ======================================

        if action["drag_end"]:

            mouse.left_up()

        # ======================================
        # Debug Text
        # ======================================

        text = "MOVE"

        if mouse.dragging:

            text = "DRAG"

        elif action["double_click"]:

            text = "DOUBLE CLICK"

        elif action["left_click"]:

            text = "CLICK"

        elif is_double:

            text = "DOUBLE CLICK"

        cv2.putText(

            frame,

            text,

            (20, 40),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0, 255, 0),

            2

        )

    else:

        if mouse.dragging:

            mouse.left_up()

    cv2.imshow(


    "KTEE Virtual Mouse",

    frame
    )

    if cv2.waitKey(1) == 27:

        break


cap.release()

cv2.destroyAllWindows()