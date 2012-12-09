# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~
This Class runs a topic
"""

from __future__ import absolute_import
from mailmove import celery, mailmove

@celery.task
def run_topic(job_uuid, topic_uuid):
    pass

@celery.task
def run_job(job_uuid):
    pass
