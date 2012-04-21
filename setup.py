#! /usr/bin/env python


from setuptools import setup


setup(
    name='mdx_outline',
    version='1.0',
    author='Alexandre Leray',
    author_email='alexandre@stdin.fr',
    description='Python-Markdown extension to wrap the document logical sections (as implied by h1-h6 headings)',
    url='http://activearchives.org/',
    py_modules=['mdx_outline'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
