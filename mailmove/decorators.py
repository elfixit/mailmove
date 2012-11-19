from functools import wraps
from flask import abort, request

from mailmove.models import Job

def job_required(f):
    """
        Checks if the job by kwarg job_uuid is available and if the users password for the job is correct
    """
    @wraps(f)
    def decorator(* args, **kwargs):
        job_uuid = kwargs.get('job_uuid', None)
        if not job_uuid:
            abort(401)
        job = Job.objects.get(_id=job_uuid)
        if job:
            if request.method == 'post':
                job_pass = request.args.get('pass')
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
        return f(args, kwargs)

    return no_robot
