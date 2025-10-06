import cv2
import time
from collections import Counter
from object_detection import detect_objects
from speech_output import speak

def format_objects(objects):
    """صياغة نص مرتب فيه عدد كل object"""
    counter = Counter([obj[0] for obj in objects])  # فقط أسماء الأجسام
    parts = []
    for obj, count in counter.items():
        if count > 1:
            parts.append(f"{count} {obj}s")
        else:
            parts.append(f"{count} {obj}")
    return ", ".join(parts)

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        speak("Camera could not be opened")
        return

    speak("Camera is running. Press Q to quit.")

    last_speak_time = 0      # للكلام العادي كل 5 ثواني
    last_warning_time = 0    # للتحذيرات كل 3 ثواني

    warning_threshold = 400  # عتبة القرب الشديد (أقرب كتير، بالبكسل)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detected_frame, objects = detect_objects(frame)

        current_time = time.time()

        if objects:
            # نتحقق من الأجسام القريبة جدًا أولاً (أولوية للتحذير)
            close_objs = [label for label, w, h in objects if w >= warning_threshold or h >= warning_threshold]

            if close_objs:
                # لو فيه جسم قريب جدًا، نتحقق من الـ 3 ثواني للتحذير
                if current_time - last_warning_time >= 3:
                    close_sentence = ", ".join(set(close_objs))
                    sentence = f"Warning, the {close_sentence} is too close"
                    speak(sentence)
                    print(sentence)
                    last_warning_time = current_time
                    last_speak_time = current_time  # نحدث الـ normal timer كمان
                continue  # ما نعملش الكلام العادي
            else:
                # مفيش جسم قريب جدًا، نتحقق من الكلام العادي كل 5 ثواني
                if current_time - last_speak_time >= 5:
                    sentence = "I see " + format_objects(objects)
                    speak(sentence)
                    print(sentence)
                    last_speak_time = current_time
        else:
            # مفيش أجسام، كلام عادي كل 5 ثواني
            if current_time - last_speak_time >= 5:
                sentence = "Nothing detected"
                speak(sentence)
                print(sentence)
                last_speak_time = current_time

        # عرض الكاميرا مع البوكسات
        cv2.imshow("Camera", detected_frame)

        # الخروج بالـ Q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            speak("Camera closed")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()