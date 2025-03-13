from SpeechManager import speechRecognition
from ResponseFromGemini import responseFromGemini
from SpeechManager import speechSaying
from SearchingKeywords import findVariants
from Localization import locationData
import time


def commandsSwitch(text):
    print(text)
    textGemini_choosing = responseFromGemini(text + "dopasuj która z kategorii: temat rozmowa,pogoda,utwórz przypomnienie,co mam zrobić będzie najbardziej dopasowan do treści wcześniejszej napisz tylko i wyłącznie kategorię bez uzasadnienia")

    fittingWords_talk = findVariants(textGemini_choosing, "rozmowa")
    fittingWords_weather = findVariants(textGemini_choosing, "pogoda")
    fittingWords_reminderSave = findVariants(textGemini_choosing, "przypomnienie")
    fittingWords_reminderRemind = findVariants(textGemini_choosing, "zrobić")

    print(fittingWords_talk)
    print(fittingWords_weather)
    print(fittingWords_reminderSave)
    print(fittingWords_reminderRemind)

    print(textGemini_choosing)

    if fittingWords_talk != 0:
        while True:
            try:
                textGemini = responseFromGemini(text)
                speechSaying(textGemini)
                text = speechRecognition()

                textGemini_choosingEnd = responseFromGemini(text + "jeżeli motyw wcześniejszej napisanego tekstu będzie zawierał słowka które będą wskazywały o chęci użytkownika o zakończeniu dyskusji wypisz koniec w przeciwnym wypadku nie pisz nic")
                fittingWords_endTalk = findVariants(textGemini_choosingEnd, "koniec")
                if fittingWords_endTalk != 0:
                    speechSaying("Dobrze, zakończmy rozmowę")
                    break
            except:
                break

            time.sleep(1)

    elif fittingWords_weather != 0:
        city, region, country = locationData()
        temp = "Jaka jest pogoda w " + city +" "+ region +" "+ country
        textGemini = responseFromGemini(temp)
        speechSaying(textGemini)

    elif fittingWords_reminderSave != 0:
        with open("reminder.txt", "a") as file:
            file.write(responseFromGemini(text + "napisz to zwiezle w formacie nazwa przypomnienia,godzina,minuta,dzien,miesiac,rok wszystko cyframi, użwyaj aktualnych dat i dodaj krótki opis przpomnienia"))
            speechSaying("Dobrze, zapisałem przypomnienie")

    elif fittingWords_reminderRemind != 0:
        with open("reminder.txt", "r") as file:
            text_temp = responseFromGemini(file.read() + "powiedz WSZYSTKIE przypomnienia które są wspomniane z WCZEŚNIEJ PODANĄ datą podaj OBOWIĄZKOWO godzine oraz minute oraz nazwę przypomnienia")
            speechSaying(text_temp)

    else:
        textGemini = responseFromGemini(text)
        speechSaying(textGemini)