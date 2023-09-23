from googletrans import Translator



# translate a spanish text to english text (by default)



def translate(text, language="en"):
    translator = Translator()
    if(language != "en"):
        translation = translator.translate(text, dest=language)
    else: 
        translation = translator.translate(text)
    return translation.text

# print(translate("Hola Mundo", "fr"))