from __future__ import absolute_import
from mailmove import config, celery

if __name__ == '__main__':
    celery.start()
