# -*- coding: utf-8 -*-

"""System Informations"""

####



import sys

####

__all__ = ['ENV']

####

def _environment():
    """Collect some useful system information"""
    data = {}
    data['os'] = sys.platform
    data['pyversion'] = '{0:x}'.format(sys.hexversion)
    data['encoding'] = sys.stdout.encoding or sys.getfilesystemencoding()
    return data

####

ENV = _environment()

####
