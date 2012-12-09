from mailmove import bcrypt
from mailmove.models import Job, Topic, Provider
from mailmove.topics.dummy.model import DummyTopic
from mailmove.topics.mail.model import MailTopic
from mailmove.providers.dummy.model import DummyProvider
from mailmove.providers.imap.model import ImapProvider
from mailmove.providers.gmail.model import GMailProvider

def make_test_data():
    job = Job()
    job.password = bcrypt.generate_password_hash("mailmove_test")
    job.status = 1
    job.set_credentials('test1', {'user': 'mailmove.test1@gmail.com', 'pass': 'mailmove_test1'})
    job.set_credentials('test2', {'user': 'mailmove.test2@gmail.com', 'pass': 'mailmove_test2'})
    job.save()

    dummy = DummyTopic()
    dummy1 = DummyProvider()
    dummy1.list.append('hallo1')
    dummy1.list.append('bye1')
    dummy2 = DummyProvider()
    dummy2.list.append('hello2')
    dummy2.list.append('bye2')
    dummy.providers.append(dummy1)
    dummy.providers.append(dummy2)
    dummy.save()

    mail = MailTopic()
    account1 = GMailProvider()
    account1.credential = 'test1'
    account2 = GMailProvider()
    account2.credential = 'test2'
    mail.providers.append(account1)
    mail.providers.append(account2)
    mail.save()

    return job

