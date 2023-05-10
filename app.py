import eel
import time
import test_microphone


import reference
from context import DW

import threading



eel.init('site')

isIn = False

k = None

p = None

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


#####################################################################################################


@eel.expose
def updateName1(value):
    eel.updateName1(value)

@eel.expose
def updateWordGuest(value):
    eel.updateWordGuest(value)

@eel.expose
def updateName2(value):
    eel.updateName2(value)

@eel.expose
def updateName3(value):
    eel.updateName3(value)


@eel.expose
def updateName4(value):
    eel.updateName4(value)


@eel.expose
def updateName5(value):
    eel.updateName5(value)

@eel.expose
def updateFrq1(value):
    eel.updateFrq1(value)

@eel.expose
def updateFrq2(value):
    eel.updateFrq2(value)

@eel.expose
def updateFrq3(value):
    eel.updateFrq3(value)

@eel.expose
def updateFrq4(value):
    eel.updateFrq4(value)

@eel.expose
def updateFrq5(value):
    eel.updateFrq5(value)

@eel.expose
def updateOccu1(value):
    eel.updateOccu1(value)

@eel.expose
def updateOccu2(value):
    eel.updateOccu2(value)

@eel.expose
def updateOccu3(value):
    eel.updateOccu3(value)

@eel.expose
def updateOccu4(value):
    eel.updateOccu4(value)

@eel.expose
def updateOccu5(value):
    eel.updateOccu5(value)

@eel.expose
def updateScore1(value):
    eel.updateScore1(value)

@eel.expose
def updateScore2(value):
    eel.updateScore2(value)

@eel.expose
def updateScore3(value):
    eel.updateScore3(value)

@eel.expose
def updateScore4(value):
    eel.updateScore4(value)

@eel.expose
def updateScore5(value):
    eel.updateScore5(value)


@eel.expose
def updateSpacy1(value):
    eel.updateSpacy1(value)

@eel.expose
def updateSpacy2(value):
    eel.updateSpacy2(value)

@eel.expose
def updateSpacy3(value):
    eel.updateSpacy3(value)

@eel.expose
def updateSpacy4(value):
    eel.updateSpacy4(value)

@eel.expose
def updateSpacy5(value):
    eel.updateSpacy5(value)


@eel.expose
def updatePos1(value):
    eel.updatePos1(value)

@eel.expose
def updatePos2(value):
    eel.updatePos2(value)

@eel.expose
def updatePos3(value):
    eel.updatePos3(value)

@eel.expose
def updatePos4(value):
    eel.updatePos4(value)

@eel.expose
def updatePos5(value):
    eel.updatePos5(value)

@eel.expose
def updateUserProfession(value):
    eel.updateUserProfession(value)

@eel.expose
def updateGuestProfession(value):
    eel.updateGuestProfession(value)

@eel.expose
def update_image(imgSrc):
    #print("yes, I did get into update_image")
    eel.updateImage(imgSrc)

@eel.expose
def updateGuestDefiniton(value):
    eel.updateGuestDefiniton(value)

@eel.expose
def updateInputText(value):
    eel.updateInputText(value)

@eel.expose
def updateGuestImage(imgSrc):
    #print("yes, I did get into update_image")
    eel.updateGuestImage(imgSrc)

@eel.expose
def searchListUpdate(value):
    eel.searchListUpdate(value)


#####==================This is context file========================
def startContext(window, fileP, userProf, guestProf):
    print("Starting Class")

    eel.sleep(5)
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

    test_microphone.start_listen()

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


    while True:
        eel.sleep(1)

        updateUserProfession(userProf)
        eel.sleep(1)
        updateGuestProfession(guestProf)
        eel.sleep(1)


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
        print("===================This is for Guest=================")
        print(wordsGuest)

        if words:
            word = words[0]

            # print("===========================Unknown Word==========================================")
            # print("**********************************************************************************")
            # print("This is the most unknown word till now: ")

            if word:
                # print(word)

                updateName1(word)

                updateFrq1(dw.input_freq[words[0]])

                updateOccu1(dw.word_freq_allwords[words[0]])

                updateSpacy1(1-dw.word_profession[words[0]])

                updatePos1(-0.00022*(dw.word_pos[words[0]] % dw.window) * (dw.word_pos[words[0]] % dw.window) + 0.00138*(dw.word_pos[words[0]] % dw.window) + 0.99883)

                updateScore1(dw.input_freq[words[0]]/dw.word_freq_allwords[words[0]] * (-0.00022*(dw.word_pos[words[0]] % dw.window) * (dw.word_pos[words[0]] % dw.window) + 0.00138*(dw.word_pos[words[0]] % dw.window) + 0.99883) * (1-dw.word_profession[words[0]]))

            else:
                print("No UNKNOWN WORDS")

            if wordsGuest:
                wordGuest = wordsGuest[0]
            else:
                print("There is no word for Guest.")

            ##================== This is updating the table===========================================#
            if len(words)>=2:
                updateName2(words[1])

                updateFrq2(dw.input_freq[words[1]])

                updateOccu2(dw.word_freq_allwords[words[1]])

                updateSpacy2(1-dw.word_profession[words[1]])

                updatePos2(-0.00022*(dw.word_pos[words[1]] % dw.window) * (dw.word_pos[words[1]] % dw.window) + 0.00138*(dw.word_pos[words[1]] % dw.window) + 0.99883)

                updateScore2(dw.input_freq[words[1]]/dw.word_freq_allwords[words[1]] * (-0.00022*(dw.word_pos[words[1]] % dw.window) * (dw.word_pos[words[1]] % dw.window) + 0.00138*(dw.word_pos[words[1]] % dw.window) + 0.99883) * (1-dw.word_profession[words[1]]))



            if len(words) >= 3:
                updateName3(words[2])

                updateFrq3(dw.input_freq[words[2]])

                updateOccu3(dw.word_freq_allwords[words[2]])

                updateSpacy3(1-dw.word_profession[words[2]])

                updatePos3(-0.00022*(dw.word_pos[words[2]] % dw.window) * (dw.word_pos[words[2]] % dw.window) + 0.00138*(dw.word_pos[words[2]] % dw.window) + 0.99883)

                updateScore3(dw.input_freq[words[2]]/dw.word_freq_allwords[words[2]] * (-0.00022*(dw.word_pos[words[2]] % dw.window) * (dw.word_pos[words[2]] % dw.window) + 0.00138*(dw.word_pos[words[2]] % dw.window) + 0.99883) * (1-dw.word_profession[words[2]]))



            if len(words) >= 4:
                updateName4(words[3])

                updateFrq4(dw.input_freq[words[3]])

                updateOccu4(dw.word_freq_allwords[words[3]])

                updateSpacy4(1-dw.word_profession[words[3]])

                updatePos4(-0.00022*(dw.word_pos[words[3]] % dw.window) * (dw.word_pos[words[3]] % dw.window) + 0.00138*(dw.word_pos[words[3]] % dw.window) + 0.99883)

                updateScore4(dw.input_freq[words[3]]/dw.word_freq_allwords[words[3]] * (-0.00022*(dw.word_pos[words[3]] % dw.window) * (dw.word_pos[words[3]] % dw.window) + 0.00138*(dw.word_pos[words[3]] % dw.window) + 0.99883) * (1-dw.word_profession[words[3]]))



            if len(words)>= 5:
                updateName5(words[4])

                updateFrq5(dw.input_freq[words[4]])

                updateOccu5(dw.word_freq_allwords[words[4]])

                updateSpacy5(1-dw.word_profession[words[4]])

                updatePos5(-0.00022*(dw.word_pos[words[4]] % dw.window) * (dw.word_pos[words[4]] % dw.window) + 0.00138*(dw.word_pos[words[4]] % dw.window) + 0.99883)

                updateScore5(dw.input_freq[words[4]]/dw.word_freq_allwords[words[4]] * (-0.00022*(dw.word_pos[words[4]] % dw.window) * (dw.word_pos[words[4]] % dw.window) + 0.00138*(dw.word_pos[words[4]] % dw.window) + 0.99883) * (1-dw.word_profession[words[4]]))

            personNames = []
            personNames = dw.get_person_names()

            if word != currentWord and dw.word_pos[word] != currentWordCount:
                sentence = dw.get_sentence(word)
                currentWord = word
                currentWordCount = dw.word_pos[word]

                if len(searchList) == 0 or word not in searchList:
                    searchList.append(word)

                wordDef = reference.get_def(word, sentence)

                if not wordDef:
                    finalDefinition = "No definition found."


                else:
                    finalDefinition = wordDef

                definitionReady = word.capitalize() +': <br>' + str(finalDefinition) +'<br>' +'<br>' + "Person Names:" + '<br>' + str(personNames)
                update_value(definitionReady)
                if (definitionReady[0] == '('):
                    reference.getPicture(word)
                else:
                    reference.getPicture(word + " " + finalDefinition)
                update_image('./image.png')



            if wordGuest != currentWordGuest and dw.word_pos[wordGuest] != currentWordGuestCount:
                guestSentence = dw.get_sentence(wordGuest)

                if len(searchList) == 0 or wordGuest not in searchList:
                        searchList.append(wordGuest)

                if wordGuest == currentWord:
                    guest_def = definitionReady
                    updateGuestDefiniton(guest_def)
                    time.sleep(0.5)
                    updateGuestImage('./image.png')

                else:
                    defineGuest = reference.get_def(wordGuest, guestSentence)
                    guest_def = wordGuest.capitalize() +': <br>' + str(defineGuest) +'<br>' +'<br>' + "Person Names:" + '<br>' + str(personNames)
                    if guest_def[0] == '(':
                        reference.getPicture(wordGuest)
                    else:
                        reference.getPictureGuest(wordGuest+ " " + guest_def)
                    updateGuestDefiniton(guest_def)
                    time.sleep(0.5)
                    updateGuestImage('./image2.png')

                # updateGuestDefiniton(guest_def)
                # time.sleep(0.5)
                # updateGuestImage('./image.png')

                currentWordGuest = wordGuest
                currentWordGuestCount = dw.word_pos[wordGuest]



        searchListUpdate(str(searchList))
        eel.sleep(1)









#####===========This is the MAIN executable file====================#####
def start_eel():

    eel.start('index.html', block=False, port=8080)
    eel.sleep(1)

start_eel()

while True:

    eel.sleep(1)

    # Please update the condition if you add for more users
    if k is not None and p is not None and isIn:
        print("The user profession is:", k)
        print("The guest profession is:", p)

        window = 150
        filePath = "./words2.txt"



        t = threading.Thread(target=startContext(window, filePath, k, p))
        t.start()
        #
        # exit()
        # exit()


    else:
        #print(isIn)
        continue

