from modeltranslation.translator import translator, TranslationOptions
from Front.models import *

class MenuTranslationOptions(TranslationOptions):
    fields=('name','text',)

translator.register(Menu, MenuTranslationOptions)