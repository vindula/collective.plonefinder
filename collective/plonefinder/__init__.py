# -*- coding: utf-8 -*-
# $Id: __init__.py 232024 2011-02-12 21:27:12Z glenfant $
"""Main product initializer
"""

import logging
from zope.i18n import MessageFactory
from collective.plonefinder import config

logger = logging.getLogger(config.PROJECTNAME)
siteMessageFactory = MessageFactory(config.PROJECTNAME)


