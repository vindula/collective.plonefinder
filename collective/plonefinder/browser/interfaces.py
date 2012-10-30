# -*- coding: utf-8 -*-
# $Id: interfaces.py 232024 2011-02-12 21:27:12Z glenfant $

from zope.interface import Interface

# FIXME: Why is this a marker interface

class IFinderUploadCapable(Interface):
    """Any container/object which supports uploading through plone_finder.
    """


