# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~

"""

from __future__ import absolute_import
from mailmove import celery, mailmove
from mailmove.models import Job, Topic

@celery.task
def test_topic(job_uuid, topic_uuid):
    pass

@celery.task
def test_job(job_uuid):
    job = Job.objects.get(id=job_uuid)
    for topic in job.topics:
        test_topic(job_uuid, topic.id)
