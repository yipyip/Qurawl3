# -*- coding: utf-8 -*-

"""
Insert Root of Project in sys.path.

All modules use absolute imports. The main application is called in the
root directory of the project. In case a module should called directly
within a subdirectory, packages contain a file 'paths.py' for inserting
root in sys.path. In this case every module needs to 'import paths' to
import other modules from the application package hierachy.
"""

####



import sys
import os

####

__all__ = ['ROOT']

####
# 1 == one level up

ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), *[os.pardir] * 1)
sys.path.insert(0, ROOT)

####
