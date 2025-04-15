# Hypervision Slot Checker 🎯

A simple Python tray bot that checks [hypervision.gg](https://hypervision.gg/checkout/?prod=1) every minute and alerts you when a slot becomes available.

## 🔔 Features

- Runs silently in the system tray
- Desktop notifications
- Loud sound alert
- Automatically opens the browser to the slot page
- No login required

## 🚀 How to Run

### Option 1: With Python

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```
2. Run the app:
   ```
   python slot_checker_app.py
   ```

### Option 2: Download `.exe` (coming soon)

No Python required! Just double-click the app.

## 🧰 Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

## 📦 Build Your Own `.exe`

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Build the executable:
   ```
   pyinstaller --noconsole --onefile --icon=icon.ico --add-data "icon.ico;." slot_checker_app.py
   ```

## ✅ Status

✔️ Fully working and tested on Windows 11.

## 📜 License

MIT
