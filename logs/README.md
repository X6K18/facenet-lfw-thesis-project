# 📝 Logs Directory

This folder stores all **log files** generated during the execution of the Face Recognition System.

---

## 📚 Purpose

The `logs/` directory is used to:

* Track system activities
* Record model predictions and errors
* Monitor real-time recognition events
* Support debugging and performance analysis

---

## 📂 Structure

Typical log files include:

* `app.log`
  → Logs from the Flask backend (API requests, responses)

* `training.log`
  → Training process (epochs, loss, accuracy)

* `error.log`
  → Runtime errors and exceptions

* `realtime.log`
  → Webcam recognition events (detected faces, timestamps)

* `attendance.log` *(optional)*
  → Records of recognized users (for attendance system)

---

## 📌 Log Format

Logs are typically stored in the following format:

```id="logfmt1"
[YYYY-MM-DD HH:MM:SS] [LEVEL] Message
```

Example:

```id="logfmt2"
[2026-04-24 10:15:32] [INFO] Face detected: John_Doe
[2026-04-24 10:15:33] [INFO] Prediction confidence: 0.92
[2026-04-24 10:15:35] [ERROR] Failed to detect face
```

---

## ⚙️ Logging Levels

The system uses standard logging levels:

* INFO → Normal system operations
* WARNING → Potential issues
* ERROR → Errors affecting functionality
* DEBUG → Detailed debugging information

---

## 🚀 Usage

Logs are automatically generated when:

* Running backend server
* Training models
* Performing real-time face recognition
* Executing API requests

---

## ⚠️ Notes

* Log files can grow large over time

* It is recommended to:

  * Rotate logs periodically
  * Clear old logs when not needed

* Logs are **not included in GitHub** by default (see `.gitignore`)

---

## 🔒 Privacy Considerations

* Logs may contain:

  * User identities (names/IDs)
  * Timestamps
* Avoid sharing logs publicly if they contain sensitive information

---

## 🛠️ Best Practices

* Use structured logging (JSON format if needed)
* Separate logs by module (backend, training, realtime)
* Monitor logs regularly for system issues

---

## 📌 Role in Project

The `logs/` folder is essential for:

* 🐞 Debugging system errors
* 📊 Analyzing model performance
* 🎥 Tracking real-time recognition events
* 📋 Supporting system evaluation in the thesis

---

## 👨‍💻 Author

* Student: *[Your Name]*
* Project: Face Recognition System using FaceNet

---

## 📅 Version

* Last updated: 2026
