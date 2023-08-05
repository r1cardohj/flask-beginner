"""
    Flask-Beginner
    -----------------
    a quick project directory maker for flask.
    :copyright: (c) 2023 by r1cardohj.
    :license: MIT, see LICENSE for more details.
"""
from os import path
from codecs import open
from setuptools import setup

basedir = path.abspath(path.dirname(__file__))

with open(path.join(basedir,'README.md'),encoding='utf-8') as f:
    long_description = f.read()
    

setup(
    name ='Flask-Beginner',
    version = '0.0.1',
    url='https://github.com/r1cardohj/flask-beginner',
    license='MIT',
    author='r1cardohj',
    author_email='2413302357@qq.com',
    description='a quick project directory maker for flask.',
    long_description=long_description,
    install_requires= ['Flask'],
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['flask_beginner'],
    zip_safe=False,
    test_suit='test',
    keywords='flask extension development',
    extras_require={
        'all':[
            'flask-login',
            'flask-wtf',
            'flask-sqlalchemy',
            'Flask-Migrate'
        ]
            
    },
    entry_points={
        'console_scripts': [
            'beginner = flask_beginner.beginner:run',
        ]
    },
)