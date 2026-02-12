# Distraction Detector

Distraction Detector is a real-time computer vision project that monitors user attention by detecting facial cues, eye gaze, and blink patterns. It is designed to help users stay focused during work, study sessions, or while driving by identifying moments of distraction and alerting them.

---

## Table of Contents

- [Features](#features)  
- [Demo](#demo)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Technologies](#technologies)  
- [Future Improvements](#future-improvements)  

---

## Features

- Detects eye gaze direction to determine focus or distraction.  
- Monitors blink rate and eye closure for fatigue detection.  
- Provides real-time alerts when distraction is detected.  
- Lightweight and fast enough for real-time monitoring.  
- Can be integrated with other productivity or safety applications.  

---

## Demo

> *(Optional: Add GIF or screenshots of your program in action)*

---

## Installation

1. Clone the repository:
git clone https://github.com/jiya-gandhi-108/distraction-detector.git
cd distraction-detector

2.Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3.Install dependencies:
pip install -r requirements.txt

4.Usage
Run the main program:
python main.py

The system will access your webcam and start monitoring for distraction.
Watch for on-screen alerts when distraction or eye closure is detected.

Project Structure

distraction-detector/
│
├── detectors/           # Core detection modules
│   ├── face_gaze.py
│   └── blink_detector.py
├── assets/              # Images, icons, or resources
├── main.py              # Entry point of the project
├── requirements.txt     # Python dependencies
└── README.md

Technologies
Python 3.8+
OpenCV (Computer Vision)
MediaPipe (Face and Eye Tracking)
NumPy
Optional: PyQt or Tkinter for GUI enhancements

Future Improvements
Add fatigue detection based on long-term blink patterns.
Integrate distraction scoring with analytics dashboards.
Enable logging and report generation for productivity tracking.
Add support for multiple cameras or remote monitoring.
