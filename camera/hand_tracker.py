import cv2
import mediapipe as mp
import math


class HandTracker:

    def __init__(
            self,
            max_hands=1,
            detection_confidence=0.75,
            tracking_confidence=0.75
    ):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(

            static_image_mode=False,

            max_num_hands=max_hands,

            model_complexity=1,

            min_detection_confidence=detection_confidence,

            min_tracking_confidence=tracking_confidence

        )


        self.drawer = mp.solutions.drawing_utils

        self.results = None



    # ==========================================
    # Find Hands
    # ==========================================

    def find_hands(self, frame):

        rgb = cv2.cvtColor(

            frame,

            cv2.COLOR_BGR2RGB

        )


        self.results = self.hands.process(rgb)



        if self.results.multi_hand_landmarks:

            for hand in self.results.multi_hand_landmarks:

                self.drawer.draw_landmarks(

                    frame,

                    hand,

                    self.mp_hands.HAND_CONNECTIONS

                )


        return frame



    # ==========================================
    # Get Landmarks
    # ==========================================

    def get_landmarks(self, frame):

        hands = []


        if self.results and self.results.multi_hand_landmarks:


            h, w, _ = frame.shape


            for hand in self.results.multi_hand_landmarks:


                one_hand = []


                for index, lm in enumerate(hand.landmark):


                    one_hand.append({

                        "id": index,

                        "x": int(lm.x * w),

                        "y": int(lm.y * h)

                    })


                hands.append(one_hand)



        return hands



    # ==========================================
    # Distance
    # ==========================================

    def distance(self, p1, p2):

        return math.hypot(

            p1["x"] - p2["x"],

            p1["y"] - p2["y"]

        )



    # ==========================================
    # Finger Detection
    # ==========================================

    def fingers_up(self, hand):

        fingers = []


        # Thumb
        if hand[4]["x"] < hand[3]["x"]:

            fingers.append(1)

        else:

            fingers.append(0)



        # Index

        if hand[8]["y"] < hand[6]["y"]:

            fingers.append(1)

        else:

            fingers.append(0)



        # Middle

        if hand[12]["y"] < hand[10]["y"]:

            fingers.append(1)

        else:

            fingers.append(0)



        # Ring

        if hand[16]["y"] < hand[14]["y"]:

            fingers.append(1)

        else:

            fingers.append(0)



        # Pinky

        if hand[20]["y"] < hand[18]["y"]:

            fingers.append(1)

        else:

            fingers.append(0)



        return fingers



    # ==========================================
    # ✌ Double Click Gesture
    # ==========================================

    def is_double_click(self, hand):

        fingers = self.fingers_up(hand)


        # Thumb, Index, Middle, Ring, Pinky

        # ✌ = [0,1,1,0,0]

        return (

            fingers[1] == 1

            and

            fingers[2] == 1

            and

            fingers[3] == 0

            and

            fingers[4] == 0

        )