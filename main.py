from SpeechManager import speechRecognition
from Commands import commandsSwitch
from PlaySound import playSound
from SearchingKeywords import findVariants

while True:
    try:
        textInit = speechRecognition()
        print(textInit)

        textInit_piksil = findVariants(textInit, "piksel")
        textInit_pixel = findVariants(textInit, "pixel")
        textInit_pixil = findVariants(textInit, "pixil")
        textInit_pixie = findVariants(textInit, "pixie")
        textInit_pixe = findVariants(textInit, "pixe")

        if textInit_piksil != 0 or textInit_pixel != 0 or textInit_pixil != 0 or textInit_pixie != 0 or textInit_pixe != 0:
            playSound("pop-268648.mp3")
            text = ""
            while text == "":
                text = speechRecognition()
            commandsSwitch(text)
    except:
        continue
