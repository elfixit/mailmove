# -*- coding: utf-8 -*-
"""
mailmove.decorators
~~~~~~~~~~~~~~~~~~~

"""
from __future__ import absolute_import
from functools import wraps
from flask import abort, request

from mailmove import bcrypt, mailmove
from mailmove.models import Job

def job_required(f):
    """
        Checks if the job by kwarg job_uuid is available and if the users password for the job is correct
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        job_uuid = kwargs.get('job_uuid', None)
        if not job_uuid:
            abort(401)
        job = Job.objects.get(_id=job_uuid)
        if job:
            check = False
            if request.method == 'post':
                job_pass = request.args.get('pass')
                if bcrypt.check_password_hash(job.password, job_pass):
                    check = True
                    mailmove.flask.session['job_pass'] = job_pass
            if mailmove.flask.session.get('job_pass', False):
                job_pass = mailmove.flask.session['job_pass']
                if bcrypt.check_password_hash(job.password, job_pass):
                    check = True
            if job and check:
                del kwargs['job_uuid']
                kwargs['job'] = job
                f(*args, **kwargs)
            elif check == False:
                abort(403)
        else:
            abort(404)

    return decorator

def no_robot(f):
    """
        this decorator shut contain in the future the information that the request doesn't come from any kind of robot..
        *currently not implemented*
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        #ToDo: later implement anti robot check..
        return f(*args, **kwargs)

    return decorator
