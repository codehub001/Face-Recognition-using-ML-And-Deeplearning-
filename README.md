# 🎭 Face Recognition-Based Attendance System

A Python GUI-integrated attendance system using face recognition to automate the attendance process efficiently.

## 📌 Overview
This project leverages **OpenCV** and **Tkinter** to build an AI-powered attendance system. By utilizing **face recognition**, it marks attendance automatically and securely stores it in CSV files.

## ✨ Features
✅ **User-Friendly GUI** - Interactive interface built with Tkinter for easy navigation.<br>
✅ **Face Recognition Technology** - Uses OpenCV's LBPHFaceRecognizer for precise detection.<br>
✅ **Secure Access** - Password-protected new user registration.<br>
✅ **Automated Attendance** - Creates a daily CSV file with accurate timestamps.<br>
✅ **Live Attendance Updates** - Displays attendance records dynamically on the main screen.<br>
✅ **Data Storage** - Stores registered user details in a structured CSV format.<br>

## 🛠️ Tech Stack
- **Python** (Core logic)
- **OpenCV** (Face Recognition & Image Processing)
- **Tkinter** (Graphical User Interface)
- **CSV, NumPy, Pandas** (Data Management & Storage)
- **Datetime** (Timestamp Handling)

## 🖥️ Installation Guide
Follow these simple steps to set up the project on your local machine:

```bash
# Clone the repository
git clone https://github.com/your-github-username/Face_Recognition_Attendance_System.git
cd Face_Recognition_Attendance_System

# Install dependencies
pip install opencv-python numpy pandas

# Run the application
python main.py
```

## 🚀 How It Works
1. **User Registration:**
   - Admin adds a new user with name and unique ID.
   - The system captures multiple face images for training.

2. **Face Training:**
   - OpenCV's **LBPHFaceRecognizer** trains the model with registered faces.

3. **Attendance Marking:**
   - The system detects faces from live webcam feed.
   - Matches them with the trained model.
   - If a match is found, attendance is recorded with date & time.
   
4. **CSV Logging:**
   - Each day's attendance is stored in a separate CSV file.

---
## 📸 Screenshots

### 🔹 Main Screen
![Main Screen](https://user-images.githubusercontent.com/37211676/58502148-97ec2a00-81a3-11e9-963e-674b9c3e05dc.png)

### 🔹 Help Option
![Help Option](https://user-images.githubusercontent.com/37211676/58502152-991d5700-81a3-11e9-861a-9115526010c2.png)

### 🔹 Change Password
![Change Password](https://user-images.githubusercontent.com/37211676/58502146-97539380-81a3-11e9-8536-0c68160ecc55.png)

---
## 📥 Installation & Usage

1️⃣ **Clone the repository**  
```bash
 git clone https://github.com/yourusername/face_recognition_attendance.git
 cd face_recognition_attendance
```

2️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

3️⃣ **Run the application**  
```bash
python main.py
```

---
## 📢 Future Enhancements

🚀 **Cloud Integration** - Store attendance data on cloud platforms like Firebase.
🚀 **Mobile App Support** - Develop an Android/iOS app for remote access.
🚀 **Multiple Camera Support** - Extend functionality to support multiple camera inputs.
🚀 **Real-Time Notifications** - Send attendance alerts via email/SMS.

## 🏆 Contributing

   We welcome contributions! Feel free to submit issues or pull requests.

---
## 📞 Connect & Support

🌐 **LinkedIn:** [@codehub01](https://www.linkedin.com/in/codehub01/)  
🔗 **GitHub:** [@codehub001](https://github.com/codehub001)  


⭐ **If you found this project useful, don't forget to give it a star!** ⭐



