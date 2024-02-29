import time
import os

# Directory Name
folderInName = str(os.path.dirname(os.path.realpath(__file__)))

# Colors
BLACK  = "\033[30m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
PURPLE = "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"
RESET  = "\033[0m"


def dotAnim(text, delayTime=0.5, amountOfTime=2):
    for time in range(amountOfTime):
        for animation in (".  ",".. ","..."):
            print(text + animation, end="\r")
            delay(delayTime)

def enterContinue(animation=True):
    return question(f"Press {GREEN}'ENTER'{RESET} to continue.", animation)

def question(text="", animation=True):
    if animation == True:
        pythonType(text)
        answer = input("\n> ")
    else:
        answer = input(text + "\n> ")
    return answer

def delay(amountOfTime=1):
    time.sleep(amountOfTime)

def clear():
    os.system("cls")

def pythonType(text, delayAmount=0.025):
    for char in text:
        print(char, end='', flush=True)
        delay(delayAmount)

def invalidOption(optionChosen, animation=True):
    optionChosen = str(optionChosen)
    if animation == True:
        pythonType("\"" + optionChosen + "\" is not one of the options. Try again.")
    else:
        print("\"" + optionChosen + "\" is not one of the options. Try again.")
    delay()

def optionsCall(answer, max, zeroOption=False):
    max += 1
    try:
        answer = int(answer)
        for option in range(max):
            if answer < max:
                if answer == option:
                    return answer
                elif answer == 0 and zeroOption == True:
                    return answer
                else:
                    continue
            else:
                invalidOption(answer)
                return None
    except:
        invalidOption(answer)
        return None

def newFeature(feature="", animation=True):
    if feature == "":
        if animation == True:
            pythonType("This feature has not been impliminted into the game just yet.")
        elif animation == False:
            print("This feature has not been impliminted into the game just yet.")
    else:
        if animation == True:
            pythonType("\"" + feature + "\" is a feature that is not yet impliminted into the game.")
        elif animation == False:
            print("\"" + feature + "\" is a feature that is not yet impliminted into the game.")


