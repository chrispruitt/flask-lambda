from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name='flask-lambda-python36-lb',
    version='0.6.0',
    description=('Python3.6+ module to make Flask compatible with AWS Gateway and AWS Load Balancer'),
    long_description=long_description,
    keywords='flask aws amazon lambda load balancer lb elb alb',
    author='Chris Pruitt',
    author_email='chris.pruitt15@gmail.com',
    url='https://github.com/chrispruitt/flask-lambda',
    license='Apache License, Version 2.0',
    py_modules=['flask_lambda'],
    install_requires=['Flask>=0.10'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
    ]
)
