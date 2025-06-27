<img width="772" alt="Screenshot 2025-06-27 at 2 06 57 PM" src="https://github.com/user-attachments/assets/730c1568-d3f0-4b5f-aa81-f65512a9517d" /># 🎨 Creative Canvas: A Computer Vision Art Project

Creative Canvas is an innovative digital drawing platform that empowers users—especially children—to create art using nothing but hand gestures and a webcam. By integrating real-time hand tracking with a seamless drawing interface, the platform lowers the barrier to digital creativity, making art more intuitive, inclusive, and fun.

## 🚀 Features

- **Real-time Hand Gesture Drawing:** Uses MediaPipe for accurate hand and fingertip tracking.
- **No Mouse or Stylus Needed:** Draw using gestures in the air with a webcam.
- **User-Friendly UI:** Built with Qt for an interactive and easy-to-navigate interface.
- **Shape Coloring for Kids:** Includes built-in geometric shapes and child-friendly pre-drawn templates.
- **Custom Shape Import:** Upload your own drawings, which are converted into sketch templates for coloring.
- **Brush Toolset:** Multiple brush styles like pencil, spray, calligraphy, and watercolor.
- **Eraser & Undo Functionality:** Easily fix mistakes or erase with finger gestures.
- **Save and Export:** Drawings can be saved in formats such as PNG, JPEG, and PDF.
- **Cross-Platform Compatibility:** Designed to work smoothly across Windows, macOS, and Linux.

## 🧠 Tech Stack

- **Languages:** Python
- **Libraries & Tools:**
  - [MediaPipe](https://google.github.io/mediapipe/) – Real-time hand and gesture detection
  - [OpenCV](https://opencv.org/) – Video frame capture and processing
  - [Qt (PyQt5/PySide2)] – GUI development
  - NumPy – Matrix and numerical operations

## 📷 How It Works

1. **Start Webcam:** Activate your webcam with one click.
2. **Hand Detection:** MediaPipe detects and tracks your hand in real-time.
3. **Gesture Mapping:** Your fingertip becomes the brush tip. Move your hand to draw.
4. **Customize Art Tools:** Choose brush types, adjust thickness, colors, and shapes.
5. **Save Artwork:** Save your creations locally in preferred formats.

## 🎯 Use Cases

- Educational tool for children to learn digital art
- Accessibility-friendly art creation for users with motor limitations
- Interactive whiteboard or remote teaching aid
- Experimental HCI (Human-Computer Interaction) interfaces

## 📊 Results & Achievements

- **98%** hand tracking accuracy tested across varied lighting and user backgrounds
- Successfully tested by users aged **6–25**, ensuring inclusivity
- Published as part of the **Mini Project Report V Semester** at **RAIT, Navi Mumbai**
- Received praise for intuitive design and ease of use

  <img width="772" alt="Screenshot 2025-06-27 at 2 06 45 PM" src="https://github.com/user-attachments/assets/52025c96-1be2-4de9-ac1d-65e27e25279e" />
  <img width="772" alt="Screenshot 2025-06-27 at 2 06 22 PM" src="https://github.com/user-attachments/assets/1d598280-7c9f-4597-8a0b-91acba1f9dbc" />
<img width="772" alt="Screenshot 2025-06-27 at 2 06 37 PM" src="https://github.com/user-attachments/assets/17d4c176-ce86-47ad-a48d-e1608a8ec985" />
<img width="804" alt="Screenshot 2025-06-27 at 2 07 14 PM" src="https://github.com/user-attachments/assets/2be481cd-d35a-4637-b540-d79524345012" />
<img width="908" alt="Screenshot 2025-06-27 at 2 05 51 PM" src="https://github.com/user-attachments/assets/3c556ffa-9407-48bb-a990-885d89a8cc2f" />
<img width="908" alt="Screenshot 2025-06-27 at 2 06 02 PM" src="https://github.com/user-attachments/assets/60a8c950-058d-43bd-8e76-3e35d93b13ff" />

## 📁 File Structure

CreativeCanvas/
├── main.py # Application entry point
├── ui/ # Qt UI files and assets
├── utils/ # Helper modules for hand tracking, drawing logic
├── assets/ # Pre-drawn templates, icons
└── README.md


## 📌 Future Scope

- Add support for multi-hand interactions (e.g., zoom, rotate)
- Introduce gesture-based UI navigation
- Integrate voice feedback for better accessibility
- Cloud saving and sharing features


