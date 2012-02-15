from modeltranslation.translator import translator, TranslationOptions
from Front.models import *
from Article.models import *

class MenuTranslationOptions(TranslationOptions):
    fields=('name','text',)

class CourseTranslationOptions(TranslationOptions):
    fields=('name',)

class ArticleTranslationOptions(TranslationOptions):
    fields=('title','text',)

translator.register(Menu, MenuTranslationOptions)
translator.register(Course, CourseTranslationOptions)
translator.register(Article, ArticleTranslationOptions)