import pynput.keyboard

def process_key_press(key):
    print(key)

# Step1 : we are creating a variable to hold listener object,
# Note : it takes a call back function as an argument

# Step 2: Process_key_press will take a key as a parameter and will print that key
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

# Step 3: then we are interracting with the listerner by using join function
with keyboard_listener:
    keyboard_listener.join()        #  join() method which allows one thread to wait until another thread completes its execution
