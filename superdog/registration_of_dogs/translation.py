from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(AboutUs)
class BdTranslationranslation(TranslationOptions):
    fieleds = ('titie', 'content')
    

