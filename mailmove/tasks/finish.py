# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~
delete database entry and delete all files irreversible, means clean up all footprints...
"""

from __future__ import absolute_import
from mailmove import celery, mailmove

@celery.task
def finish_topic(job_uuid, topic_uuid):
    pass

@celery.task
def finish_job(job_uuid):
    pass
