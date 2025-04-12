# 🖐️ AI-Powered Virtual Keyboard

**Presented At**: Ingenious 2025 – National Level Technical Event  
**Institution**: KLE Technological University  
**Team**: Tech Titans  

---

## 🧠 Introduction

The **Virtual Keyboard** is an AI-powered solution designed to provide a **contactless typing interface** using real-time **hand gesture recognition** and **speech-to-text translation**. It simulates a keyboard on the screen that users can interact with using just their fingers—no physical keyboard required.

This project is especially useful in:
- Hygienic environments like **hospitals** and **laboratories**
- Assisting individuals with **mobility impairments**
- Compact and **portable typing setups**

---

## 🎯 Key Features

- **Virtual Keyboard Interface**: A visual keyboard layout appears on the screen with clickable buttons.
- **Gesture Typing**: Users type by bringing their **index (2nd)** and **middle (3rd)** fingers together on a key. The gesture is detected using a **webcam** and **MediaPipe**.
- **Speech Typing (Voice Input)**: By activating the “Mic” button with a gesture, users can:
  - Speak in **Hindi**
  - The system will recognize speech using Google’s **SpeechRecognition API**
  - Translate it to **English**
  - Automatically type the translated text
- **Contactless & Hygienic**: Perfect for environments requiring cleanliness or sterility.

---

## 🛠 How to Use

1. **Launch the application**:

   ```bash
   python virtual_keyboard.py


Typing using gestures:

Place your 2nd and 3rd fingers (index and middle) above a key on the virtual keyboard.

Join both fingers together while hovering over a key.

If the gesture is detected, the key is considered "pressed" and typed.

Voice typing:

Hover and “press” the Mic button using the same finger gesture.

Speak in Hindi.

The system will translate and type the recognized English text.

🧩 Technology Stack
Component	Library Used
Hand Detection	MediaPipe
Video Processing	OpenCV
Virtual UI	OpenCV
Speech Recognition	SpeechRecognition
Translation	Googletrans
UI Control	pyautogui, pygetwindow, pywin32
🧬 Architecture Overview
Modules:
Camera Module: Captures real-time frames

Hand Tracking: Detects hand landmarks via MediaPipe

Virtual Keyboard UI: Displays keys as interactive buttons

Gesture Detection: Checks when fingers are joined above a button

Voice Recognition Module: Recognizes and translates speech on mic activation

Typing Module: Sends recognized input to the active application

🌟 Motivation & Impact
🔒 Contactless Typing – Ideal for cleanroom and medical environments

♿ Accessible Design – Helps users with motor impairments

🧳 Portability – No need for bulky input hardware

🧠 Innovation in HCI – Intuitive, futuristic human-computer interaction

📦 Installation
Clone the repository:

bash
Copy
Edit
git clone gh repo clone Tech-Titans21/virtual-keyboard
cd virtual-keyboard
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

yaml
Copy
Edit

---

### 📁 Also Create These Files:

#### ✅ `requirements.txt`
```txt
opencv-python
mediapipe
SpeechRecognition
googletrans==4.0.0rc1
pygetwindow
pywin32
pyautogui
✅ Rename your script to: virtual_keyboard.py
Then initialize your GitHub repository like this:

bash
Copy
Edit
git init
git add .
git commit -m "Initial commit - Virtual Keyboard for Ingenious 2025"
git remote add origin https://github.com/your-username/virtual-keyboard.git
git push -u origin main
