import argostranslate.package, argostranslate.translate
from deep_translator import GoogleTranslator

def translate(text, to_lang):
    try:
        argostranslate.package.update_package_index()
        packages = argostranslate.package.get_installed_packages()
        for pkg in packages:
            if pkg.to_code == to_lang:
                return argostranslate.translate.translate(text, "en", to_lang)
        # If not found, fallback to Google Translate
        print("Falling back to Google Translate...")
        return GoogleTranslator(source="auto", target=to_lang).translate(text)
    except Exception as e:
        print(f"Argos Translate error: {e}")
        try:
            return GoogleTranslator(source="auto", target=to_lang).translate(text)
        except Exception as g:
            print(f"Google Translate fallback failed: {g}")
            return "Translation failed."
