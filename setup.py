import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires=[
    'distribute',
    'Flask>=0.8',
    'celery>=3.0',
    'celery-with-mongodb',
    'Flask-MimeRender',
    'Flask-Testing',
    'flask-mongoengine',
    'flask-bcrypt',
    'Flask-Script',
    #'Flask-SeaSurf',
    'pysqlite',
    'mongoengine'
    #"https://github.com/OfflineIMAP/offlineimap/tarball/master==dev"
]

tests_requires = requires + [
    'unittest2',
    'nose'
]

setup(name='mailmove',
      version='0.1',
      description='mailmove',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='mailmove community',
      author_email='mailmove@lists.xiala.net',
      url='https://mailmove.xiala.net',
      keywords='web imap sync flask',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_requires,
      test_suite="nose.collector",
)
