# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~

"""

from __future__ import absolute_import
from mailmove import app, mailmove
from flask.ext.script import Manager
from celery.apps.worker import Worker


manager = Manager(app)

@manager.command
def runcelery():
    work = Worker()
    work.run()

if __name__ == '__main__':
    mailmove.setup_from_settings()
    manager.run()
