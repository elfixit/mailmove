# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~

"""

from __future__ import absolute_import
from mailmove import celery, mailmove

@celery.task
def finish_topic(job_uuid, topic_uuid):
    pass

@celery.task
def finish_job(job_uuid):
    pass
