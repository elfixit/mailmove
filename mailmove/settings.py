# default flask config
DEBUG = True
SECRET_KEY = "3\x99nTD\x97\x82\x91l?\x16M?\x80\x99\xc9\xa4e\xac\xdd\xb8!\xea\x00\xa3\x81(\x9d\x8a;"


MONGODB_DB = "mailmove"
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017


#default celery config
BROKER_URL = 'mongodb://localhost'
CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": MONGODB_HOST,
    "port": MONGODB_PORT,
    "database": MONGODB_DB,
    "taskmeta_collection": "taskmeta"
}

#mailmove
TOPICS = (
    'mailmove.topics.mail.MailTopic',
    'mailmove.topics.dummy.DummyTopic',
)

DUMMY_PROVIDER = (
    'mailmove.provider.dummy'
)

MAIL_PROVIDER = (
    'mailmove.providers.imap.IMAP',
    #'mailmove.topics.mail.providers.GMAIL',
)


#ADDRESS_PROVIDER = (
#    'mailmove.topics.address.providers.CardDav',
#)
