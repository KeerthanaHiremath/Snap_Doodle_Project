# 🤳 Snap Doodle 🎨

**Snap Doodle** is a fun Snapchat-style face filter app using **Python**, **OpenCV**, and **CVZone**. It detects faces in real-time using your webcam and overlays transparent doodles (like sunglasses, hats, etc.) for a cool effect.

## 🧠 Features

- Face Detection
- Real-time Webcam Access
- Transparent PNG Overlay
- Lightweight & Interactive UI
- Press `q` to Quit

## 🛠️ Tech Stack

- **Python**
- **OpenCV (`cv2`)**
- **CVZone**
- **Haarcascade Classifier**

## 📁 Project Structure

```
snap-doodle/
├── main.py                        # Main application script
├── flower.png                     # Example filter image (with alpha)
├── haarcascade_frontalface_default.xml
└── README.md
```



## 🎮 Controls

- **Press S → Save snapshot**
- **Press Q → Quit the application**

## ✅ What I Learned

**This project helped me understand:**
   
   - Real-time webcam input processing with OpenCV
   - Face detection using Haar Cascades
   - Overlaying transparent images using cvzone.overlayPNG
   - Working with image formats and alpha channels (RGBA)
   - Writing interactive computer vision applications in Python
   - Basic error handling and modular code design

