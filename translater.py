from googletrans import Translator, LANGUAGES

def translate_text(text, target_lang):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"

def detect_language(text):
    translator = Translator()
    result = translator.detect(text)
    return f"Виявлено (мова={result.lang}, впевненість={result.confidence})"

def get_language_code(lang):
    if lang.lower() in LANGUAGES:
        return lang.lower()
    for code, language in LANGUAGES.items():
        if lang.lower() == language.lower():
            return code
    return "Мова не знайдена"

if __name__ == "__main__":
    text = input("Введіть текст для перекладу: ")
    target_lang = input("Введіть цільову мову (наприклад, українська або uk): ")

    print(text)
    print(detect_language(text))
    print(translate_text(text, get_language_code(target_lang)))
    print(get_language_code(target_lang))