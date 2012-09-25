from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('mailmove')

def my_view(request):
    return {'project':'mailmove'}
