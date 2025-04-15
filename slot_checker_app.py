import time
import requests
import webbrowser
import threading
import winsound
from bs4 import BeautifulSoup
from plyer import notification
from PIL import Image
import pystray
import sys
import os

# === CONFIG ===
URL = "https://hypervision.gg/checkout/?prod=1"
CHECK_INTERVAL = 60
ALERT_REPEAT_INTERVAL = 10
ICON_PATH = "icon.ico"

# === STATE FLAGS ===
alerting = False
stop_app = False
tray_icon = None  # reference to pystray icon

def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.abspath(filename)

def play_sound():
    duration = 1000
    freq = 1200
    winsound.Beep(freq, duration)

def repeat_alert():
    while alerting and not stop_app:
        play_sound()
        print("🔔 SLOT FOUND! CHECK THE WEBSITE!")
        if tray_icon:
            tray_icon.title = "🟢 Slot FOUND! Click browser!"
        time.sleep(ALERT_REPEAT_INTERVAL)

def notify_user():
    global alerting
    alerting = True

    notification.notify(
        title="Slot Available!",
        message="Go to hypervision.gg and grab your spot!",
        timeout=10
    )

    webbrowser.open(URL)
    threading.Thread(target=repeat_alert, daemon=True).start()

def check_slot():
    try:
        if tray_icon:
            tray_icon.title = "🔄 Checking for slot..."
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        if "No slots left" not in soup.text and not alerting:
            notify_user()
        elif tray_icon:
            tray_icon.title = "❌ No slot - still watching..."
    except Exception as e:
        print(f"Error: {e}")
        if tray_icon:
            tray_icon.title = f"⚠️ Error: {e}"

def start_checking():
    print("🔍 Slot checker started.")
    while not stop_app and not alerting:
        check_slot()
        time.sleep(CHECK_INTERVAL)

def quit_app(icon, item):
    global stop_app
    stop_app = True
    icon.stop()
    print("🛑 Exiting app...")
    sys.exit()

def setup_tray():
    global tray_icon
    icon_image = Image.open(resource_path(ICON_PATH))
    menu = pystray.Menu(pystray.MenuItem("Quit", quit_app))
    tray_icon = pystray.Icon("SlotChecker", icon_image, "Slot Checker - Loading...", menu)
    threading.Thread(target=start_checking, daemon=True).start()
    tray_icon.run()

if __name__ == "__main__":
    setup_tray()
