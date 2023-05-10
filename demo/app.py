import eel
import time
import test_microphone
import shutil
import os

import wordDisp


import reference
from context import DW

import threading



eel.init('site')

isIn = False

k = None

p = None

shouldRun = True

@eel.expose
def button_clicked(value):
    # print(f'The value of the button clicked is: {value}')
    global k
    k = value
    update_Val()
    return k

######This TAKES THE PROFESSION OF THE GUEST###############
@eel.expose
def button_guest(value):
    # print(f'The value of the button clicked is: {value}')
    global p
    p = value

    update_Val()
    return p

## ========== This tells that it has hit the correct HTML page=========================#############
@eel.expose
def update_Val():

    global isIn
    isIn = True


@eel.expose
def update_value(value):
    eel.updateText(value)


##==================This tells that the listening Now DOM is active ==============================######
# @eel.expose
# def loadingMicReady():
#     print("JavaScript is ready")
#     eel.loadListening()


##===============This indicates that the Listening Mic DOM is active===========================#####
@eel.expose
def listeningReady():
    print("JavaScript is ready")
    eel.loadResult()


#####################################################################################################0
@eel.expose
def updateUserProfession(value):
    eel.updateUserProfession(value)

# @eel.expose
# def updateGuestProfession(value):
#     eel.updateGuestProfession(value)

@eel.expose
def update_image(imgSrc):
    print("yes, I did get into update_image")
    eel.updateImage(imgSrc)

def loadingMicReady():
    print("JavaScript is ready")
    eel.loadListening()


# @eel.expose
# def updateGuestDefiniton(value):
#     eel.updateGuestDefiniton(value)

@eel.expose
def updateInputText(value):
    eel.updateInputText(value)

# @eel.expose
# def updateGuestImage(imgSrc):
#     #print("yes, I did get into update_image")
#     eel.updateGuestImage(imgSrc)
#
# @eel.expose
# def searchListUpdate(value):
#     eel.searchListUpdate(value)

########==================This is for RESET==================================
@eel.expose
def reset_selection():
    global k, p, shouldRun, countMic
    k = None
    p = None
    countMic = 100000

    shouldRun = False


countMic = 0


#####==================This is context file========================
def startContext(window, fileP):

    global k, p, countMic

    userProf = k
    guestProf = p
    print("Starting Class")
    global shouldRun
    eel.sleep(1)
    finalProfession = []
    if (userProf == "Engineering"):
        profession = "Engineer developer mechanics mechanism engineer coder physics mechatronics mechanical"
    elif userProf == "Medicine":
        profession = "Doctor medicine hospitals nurses patients treatment"
    elif userProf == "Finance":
        profession = "money banks financial finance stock stocks gains deposit"
    elif userProf == "Law":
        profession = "law legal lawyer cases criminal criminals judiciary judge jurisdiction"

    finalProfession.append(profession)

    if (guestProf == "Engineering"):
        professionGuest = "Engineer developer mechanics mechanism engineer coder physics mechatronics mechanical"
    elif guestProf == "Medicine":
        professionGuest = "Doctor medicine hospitals nurses patients treatment"
    elif guestProf == "Finance":
        professionGuest = "money banks financial finance stock stocks gains deposit"
    elif guestProf == "Law":
        professionGuest = "law legal lawyer cases criminal criminals judiciary judge jurisdiction"

    finalProfession.append(professionGuest)

    dw = DW (window, fileP, professionGuest)

    if countMic == 0:
        print("Mic is true")
        test_microphone.start_listen()


    if not os.path.exists("./img_Store"):
        os.makedirs("./img_Store")

    searchList = []

    print("Class Created and Display is active.")

    dw.user_inputs(finalProfession)

    text = "" #This is our growing text

    currentWord = ""
    currentWordGuest = ""

    currentWordCount = 0
    currentWordGuestCount = 0


    listeningReady()
    eel.sleep(1)


    count = 0

    loadingMicReady()
    eel.sleep(1)


    while shouldRun:
        eel.sleep(1)

        updateUserProfession(userProf)
        eel.sleep(1)
        # updateGuestProfession(guestProf)
        # eel.sleep(1)


        text = text + test_microphone.tmp

        lenText = text.split()

        if len(lenText) > window:
            lastWords = lenText[-window:]

            text = ' '.join(lastWords)



        if not text:
            continue

        test_microphone.tmp = ""
        filePathSize = len(text)
        firstLetter = text[0]

        if not firstLetter.isalpha():
            if filePathSize <= 1:
                print("Is empty. Trying Again in sometime...")
                time.sleep(2)
                continue

        dw.text_input(text)

        input = "Input: " + dw.window_text


        if (count == 0):
            listeningReady()
            eel.sleep(1)
            count = 1



        updateInputText(input)
        eel.sleep(1)

        # print("===========================All unknown words:=========================================")
        # print("**********************************************************************************")
        words = dw.sorted_unique
        wordsGuest = dw.sorted_unique_guest

        print("==========This is for user===========================")
        print(words)


        if words:
                word = words[0]

                personNames = []
                personNames = dw.get_person_names()

                if word != currentWord or dw.word_pos[word] != currentWordCount:
                    sentence = dw.get_sentence(word)
                    currentWord = word
                    currentWordCount = dw.word_pos[word]



                    wordDef = reference.get_def(word, sentence)

                    if not wordDef:
                        finalDefinition = "No definition found."


                    else:
                        finalDefinition = wordDef

                    definitionReady = word.capitalize() +': <br>' + str(finalDefinition) +'<br>' +'<br>' + "Person Names:" + '<br>' + str(personNames)
                    update_value(definitionReady)
                    eel.sleep(1)
                    if "(" in definitionReady:
                        reference.getPicture(word)
                    else:
                        reference.getPicture(word + " " + str(finalDefinition))
                    update_image('./image.png')
                    eel.sleep(1)

                    if len(wordDisp.word_data) == 0 or word not in wordDisp.word_data:
                        img_path = "./site/image.png"
                        new_image_path = os.path.join("./img_Store/",f"{word}.png" )
                        shutil.copy(img_path, new_image_path)
                        wordDisp.add_word(word, str(finalDefinition), new_image_path)

    print("I am out.")


#####===========This is the MAIN executable file====================#####
def start_eel():

    eel.start('index.html', block=False, port=8080)
    eel.sleep(1)


def start():


    start_eel()


    while True:



        eel.sleep(1)

        global shouldRun

        shouldRun = True

        # Please update the condition if you add for more users
        if k is not None and p is not None and isIn:
            print("The user profession is:", k)
            print("The guest profession is:", p)

            window = 30
            filePath = "./words2.txt"



            t = threading.Thread(target=startContext(window, filePath))
            t.start()
            #
            # exit()
            # exit()


        else:
            #print(isIn)
            continue

start()