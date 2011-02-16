from setuptools import setup

setup(
    name='django-dnt',
    version='0.1.0',
    description='Make Django requests aware of the DNT header.',
    long_description=open('README.rst').read(),
    author='James Socol',
    author_email='james@mozilla.com',
    url='http://github.com/mozilla/django-dnt',
    license='BSD',
    packages=['dnt'],
    include_package_data=True,
    package_data = { '': ['README.rst'] },
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
