from distutils.core import setup
import re
import upsidedown

VERSION = str(upsidedown.__version__)
(AUTHOR, EMAIL) = re.match('^(.*?)\s*<(.*)>$', upsidedown.__author__).groups()
URL = upsidedown.__url__
LICENSE = upsidedown.__license__

setup(name='upsidedown',
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description='"Flip" characters in a string to create an "upside-down" impression.',
    long_description=open('README').read().decode('utf8'),
    url=URL,
    download_url='http://github.com/cburgmer/upsidedown/downloads',
    py_modules=['upsidedown'],
    license=LICENSE,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
	'Topic :: Text Processing',
        ])
