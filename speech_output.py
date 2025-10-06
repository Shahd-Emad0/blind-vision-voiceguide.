import winsound
import pyttsx3
import threading
import time

def speak(text, with_beep=True):
    def run():
        try:
            if with_beep:
                winsound.Beep(1000, 200)  # beep قصير
            engine = pyttsx3.init()
            engine.setProperty("rate", 150)   # سرعة الكلام
            engine.setProperty("volume", 1.0) # أعلى صوت
            engine.say(text)
            engine.runAndWait()
            time.sleep(0.1)  # تأخير بسيط بعد الكلام
        except Exception as e:
            print(f"Speech error: {e}")
    t = threading.Thread(target=run)
    t.start()