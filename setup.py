from distutils.core import setup
setup(name='upsidedown',
    version='0.1',
    author='Christoph Burgmer',
    author_email='cburgmer@ira.uka.de',
    description='"Flip" characters in a string to create an "upside-down" impression.',
    long_description=open('README').read().decode('utf8'),
    download_url='http://github.com/cburgmer/upsidedown/downloads',
    py_modules=['upsidedown'],
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
	'Topic :: Text Processing',
        ])
