import cv2
import mediapipe as mp
from time import sleep
import math
import speech_recognition as sr
import asyncio
from googletrans import Translator
import pygetwindow as gw
import win32gui
import win32con
import pyautogui  # Added for sending keystrokes

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width of the video frame
cap.set(4, 720)  # Set height of the video frame.

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
    ["Space", "Backspace", "Enter", "Mic"]
]

final_text = ""
line_spacing = 30


def set_window_on_top():
    hwnd = win32gui.FindWindow(None, "Image")  # OpenCV window title
    if hwnd:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def recognize_and_translate_speech():
    global final_text
    recognizer = sr.Recognizer()
    translator = Translator()
    recognizer.energy_threshold = 400
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("Calibrating for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Calibration complete. Speak now!")

        try:
            print("Listening...")
            audio = recognizer.listen(source, phrase_time_limit=5)
            detected_text = recognizer.recognize_google(audio, language='en')
            print("Detected Speech:", detected_text)

            loop = asyncio.get_event_loop()
            translated_text = loop.run_until_complete(
                translator.translate(detected_text, src='hi', dest='en')
            )
            print("Translated to English:", translated_text.text)
            final_text = translated_text.text + " "
            pyautogui.write(final_text)
        except sr.UnknownValueError:
            print("Could not understand the audio. Please speak clearly.")
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
        except Exception as e:
            print("Error:", str(e))


class Button:
    def __init__(self, pos, text, size=[100, 100]):  # Corrected __init__
        self.pos = pos
        self.size = size
        self.text = text

    def draw(self, img, color=(0, 0, 0)):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.size[0], self.pos[1] + self.size[1]), color, cv2.FILLED)
        font_scale = 1
        font_thickness = 3
        text_size = cv2.getTextSize(self.text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
        text_x = self.pos[0] + (self.size[0] - text_size[0]) // 2
        text_y = self.pos[1] + (self.size[1] + text_size[1]) // 2
        cv2.putText(img, self.text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255),
                    font_thickness, cv2.LINE_AA)
        return img


buttonList = []
for i, row in enumerate(keys):
    for j, key in enumerate(row):
        if key == "Space":
            buttonList.append(Button([75 * j + 50, 75 * i + 50], key, size=[400, 65]))
        elif key == "Backspace":
            buttonList.append(Button([75 * j + 450, 75 * i + 50], key, size=[165, 65]))
        elif key == "Enter":
            buttonList.append(Button([75 * j + 600, 75 * i + 50], key, size=[130, 65]))
        elif key == "Mic":
            buttonList.append(Button([75 * j + 750, 75 * i + 50], key, size=[120, 65]))
        else:
            buttonList.append(Button([75 * j + 50, 75 * i + 50], key, size=[65, 65]))


def find_distance(pt1, pt2):
    return math.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)


# Function to send keystrokes to active application
def send_keystrokes(key):
    if key == "Space":
        pyautogui.write(" ")
    elif key == "Backspace":
        pyautogui.press("backspace")
    elif key == "Enter":
        pyautogui.press("enter")
    elif button.text == "Mic":
        print("Mic button pressed")
        recognize_and_translate_speech()
    else:
        pyautogui.write(key)  # Sends the typed letter to the active application


while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from webcam")
        break
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    set_window_on_top()

    lmList = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            h, w, c = img.shape
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

    for button in buttonList:
        color = (0, 0, 0)
        img = button.draw(img, color)

    if len(lmList) >= 13:
        index_tip = (lmList[8][1], lmList[8][2])
        middle_tip = (lmList[12][1], lmList[12][2])
        distance = find_distance(index_tip, middle_tip)

        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            tip_x, tip_y = index_tip
            if distance < 60 and x < tip_x < x + w and y < tip_y < y + h:
                color = (0, 255, 0)
                cv2.rectangle(img, button.pos, (x + w, y + h), color, cv2.FILLED)

                send_keystrokes(button.text)  # Sends key press to active window

                sleep(0.50)
                break

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()