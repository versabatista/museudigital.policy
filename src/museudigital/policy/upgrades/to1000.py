# -*- coding: utf-8 -*-

import logging

from Products.CMFCore.utils import getToolByName

from museudigital.policy.config import PROJECTNAME

logger = logging.getLogger(PROJECTNAME)


def upgrade0to1000(context):
    """Upgrade from version 0 to version 1000.
    """
    gtool = getToolByName(context, 'portal_groups')

    gtool.addGroup('Soap', title='Soap Users', roles=roles_soap)

    # create new group for soap admin
    gtool.addGroup('Soap Admin', title='Soap Administrator', roles=roles_soap_admin)
