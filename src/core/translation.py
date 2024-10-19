from modeltranslation.translator import translator, TranslationOptions
from core.models import Book

class NewsTranslationOptions(TranslationOptions):
    fields = ('name','author','description',)

translator.register(Book, NewsTranslationOptions)