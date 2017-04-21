# -*- coding: utf-8 -*-

# A very simple setup script to create a single executable
#
# 八卦板爬蟲.py is a very simple 'Hello, world' type script which also displays the
# environment in which the script runs
#
# How to USE this ?
# Install cx_Freeze by running the command 'python -m pip install cx_Freeze --upgrade' 
# Run the build process by running the command 'python setup.py build'
# If you enconter install error, you can try command 'python -m pip install --upgrade pip' to upgrade your pip version
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

from cx_Freeze import setup, Executable

executables = [
    Executable('八卦板爬蟲.py')
]

setup(name='八卦板爬蟲',
      version='0.1',
      description='Sample cx_Freeze script',
      executables=executables
      )
