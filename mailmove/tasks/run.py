from mailmove.app import MailMove

celery = MailMove().celery

@celery.task
def run_topic(job_uuid, topic_uuid):
    pass

@celery.task
def run_job(job_uuid):
    pass
