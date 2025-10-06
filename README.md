BlindVision-VoiceGuide

Overview
BlindVision-VoiceGuide is an AI-powered assistive tool designed to empower visually impaired individuals by detecting everyday objects in real-time and announcing them aloud through text-to-speech (TTS). Built during my internship, it uses computer vision models like YOLO to analyze camera feeds, identify surroundings (e.g., "I see a chair"), and provide instant audio guidance—including urgent warnings when objects are too close (e.g., "Warning: person too close"). This makes navigation safer and more independent without relying on human help, turning a smartphone or webcam into a reliable guide for daily tasks like avoiding obstacles or locating items.

Why It's Helpful, Unique, and Important
Helpful: Enhances mobility with real-time audio alerts and proximity warnings, reducing accidents, boosting confidence, and supporting self-reliance in homes, streets, or offices.
Unique: Unlike generic screen readers, it offers proactive object detection with distance-aware voice guidance, optimized for hands-free use on portable devices.
Important: Addresses vision impairment affecting over 2.2 billion people worldwide (WHO data), promoting inclusive AI for social good and demonstrating practical innovation in computer vision and TTS.

Features
Real-Time Object Detection: Uses YOLOv8 (or similar) to identify common objects like chairs, doors, people, and obstacles from live camera input.
Audio Announcements: Integrates TTS (e.g., pyttsx3 or gTTS) to vocalize detections naturally (e.g., "I see a chair ahead").
Proximity Warnings: Estimates object distance via bounding box analysis or depth cues, issuing urgent alerts for close hazards (e.g., "Warning: obstacle too close—stop!").
Cross-Platform: Runs on desktops (with webcam) or mobiles (via compatible frameworks like Streamlit or Flask apps).
Customizable: Adjustable confidence thresholds, voice speed, and object categories for personalized use.

Tech Stack
Computer Vision: YOLO (Ultralytics library), OpenCV for video processing.
Text-to-Speech: pyttsx3 (offline) or Google TTS (online).
Language: Python 3.8+.
Dependencies: NumPy, Pillow; optional: Streamlit for a web demo interface.
Hardware: Any device with a camera (webcam, smartphone camera via API).

Installation
1. Clone the Repository:
git clone https://github.com/yourusername/BlindVision-VoiceGuide.git
cd BlindVision-VoiceGuide

2. Set Up Virtual Environment (Recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:
pip install -r requirements.txt
(Create a requirements.txt file with: ultralytics opencv-python pyttsx3 numpy pillow – adjust as needed.)

4. Download YOLO Weights (if not included):
- Run the script once; it auto-downloads pretrained models from Ultralytics.

Usage
1. Run the App:
python main.py
- This opens your camera, starts detection, and enables audio output.
- Press 'q' to quit (in desktop mode).

2. Example Output:
- Detection: Camera scans → YOLO identifies object → TTS announces.
- For warnings: If an object is within ~1m (configurable), it triggers an alert tone + voice.

3. Customization:
- Edit config.py for object classes, warning thresholds, or TTS voice.
- For mobile deployment: Use tools like Kivy or BeeWare to package as an app.

Demo
Add a demo video or GIF here to showcase the tool in action.

Contributing
Contributions are welcome! If you'd like to improve features (e.g., add more languages, better depth sensing with LiDAR), please:
1. Fork the repo.
2. Create a feature branch (git checkout -b feature/amazing-feature).
3. Commit changes (git commit -m 'Add amazing feature').
4. Push to the branch (git push origin feature/amazing-feature).
5. Open a Pull Request.

For issues or suggestions, open a GitHub issue.

License
This project is licensed under the MIT License – see the LICENSE file for details.

Acknowledgments
- Built during my internship at an AI-focused organization.
- Thanks to Ultralytics for YOLO, OpenCV community, and TTS libraries.
- Inspired by accessibility needs and WHO vision impairment stats.
- Shoutout to open-source contributors making AI inclusive!
