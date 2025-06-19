import cv2
import cvzone
import os
from datetime import datetime

# Load Haar Cascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the single filter
filter_path = 'filters/cool.png'
filter_path = 'cool.png'
cool_filter = cv2.imread(filter_path, cv2.IMREAD_UNCHANGED)

# Start webcam
cap = cv2.VideoCapture(0)

print("🎮 Controls:")
print("Press 'S' to save a snapshot")
print("Press 'Q' to quit")

while True:
    success, frame = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        try:
            # Resize the filter to fit the face
            overlay = cv2.resize(cool_filter, (int(w * 1.5), int(h * 1.5)))
            frame = cvzone.overlayPNG(frame, overlay, [x - 45, y - 75])
        except Exception as e:
            print(f"Overlay error: {e}")

    # Show filter name
    cv2.putText(frame, "Filter: cool.png", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.imshow("😎 Snap Doodle - Cool Filter", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f"snap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(filename, frame)
        print(f"✅ Snapshot saved: {filename}")

cap.release()
cv2.destroyAllWindows()