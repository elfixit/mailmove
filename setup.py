import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires=[
    'distribute',
    'unittest2',
    'Flask>=0.8',
    'celery>=3.0',
    'Flask-MimeRender',
    'Flask-Testing',
    #'Flask-SeaSurf',
    'pysqlite',
    #"https://github.com/OfflineIMAP/offlineimap/tarball/master==dev"
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
      tests_require=requires,
      test_suite="mailmove.tests",
)
