from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator('WX5QxT0LPx4I-XlvP2tGnsxmHhPg0uBa7YTMiNmoqQTf')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/12eba94b-1b96-43da-86bf-d3f5961362dc' )

def english_to_french(english_text):
    '''Translation of english to french'''
    french_translation=language_translator.translate(
        text=english_text,model_id='em-fr').get_result()
    french_text=french_translation['transalations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Translation of french to english'''
    eng_translation = language_translator.translate(
        text=french_text,model_id='fr-en').get_result()
    english_text=eng_translation['translations'][0]['translation']
    return english_text
    