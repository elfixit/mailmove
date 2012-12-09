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
    """
        This is the Test a Topic Task
        -----------------------------

        This method uses the MongoEngine Object Model Factory the find the right model and from there the controller
    """
    topic = Topic.objects.get(id=topic_uuid)
    controller = topic.get_controller()
    controller.test()

@celery.task
def test_job(job_uuid):
    job = Job.objects.get(id=job_uuid)
    for topic in job.topics:
        test_topic(job_uuid, topic.id)
