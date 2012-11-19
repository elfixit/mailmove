from mailmove.app import MailMove

celery = MailMove().celery

@celery.task
def finish_topic(job_uuid, topic_uuid):
    pass

@celery.task
def finish_job(job_uuid):
    pass
