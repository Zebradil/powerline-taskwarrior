# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name='powerline-taskwarrior',
    description='Powerline segments for showing information from the Taskwarrior task manager',
    version='0.2',
    keywords='powerline taskwarrior context prompt',
    license='MIT',
    author='German Lashevich',
    author_email='german.lashevich@gmail.com',
    url='https://github.com/zebradil/powerline-taskwarrior',
    download_url='https://github.com/zebradil/powerline-taskwarrior/tarball/0.2',
    packages=['powerline_taskwarrior'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
