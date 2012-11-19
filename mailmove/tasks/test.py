from mailmove.app import MailMove

celery = MailMove().celery

@celery.task
def test_topic(job_uuid, topic_uuid):
    pass

@celery.task
def test_job(job_uuid):
    pass
