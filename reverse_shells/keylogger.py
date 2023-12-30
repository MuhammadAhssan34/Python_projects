from pynput import keyboard

def on_press(key):
    try :
        print(f'alphanumeric key {key.char} pressed  '.format(key.char))

    except AttributeError :
        # print(f'special key {key} pressed'.format(key))
        pass
def on_release(key):
    # print(f'{0} released '.format(key))

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release)as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()