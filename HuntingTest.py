'''
import random
import threading





def get_user_input(sound, input_ready):
    """Gets user input while the timer is running."""
    pressed = input("TYPE " + sound + ": ")
    input_ready.append(pressed)

def check(sound, pressed):
    """Checks if the user's input matches the sound."""
    if pressed and sound == pressed[0]:
        print("DONE")
    else:
        print("WRONG! The correct sound was: " + sound)
#-------------------------------------------------------
def six140():
    """Main game function."""
    rand = random.randint(0, 3)
    gun_sounds = ["BANG", "BLAM", "POW", "WHAM"]
    sound = gun_sounds[rand]


    # Create a list to store user input
    input_ready = []


    # Get user input in the main thread
    get_user_input_thread = threading.Thread(target=get_user_input, args=(sound, input_ready))
    get_user_input_thread.start()

    # Wait for both threads to finish
    get_user_input_thread.join()

    # Check the input after both threads are done
    check(sound, input_ready)

six140() #LINE 3120
'''