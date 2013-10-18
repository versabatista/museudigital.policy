# -*- coding: utf-8 -*-

import logging

from Products.CMFCore.utils import getToolByName

from museudigital.policy.config import PROJECTNAME

logger = logging.getLogger(PROJECTNAME)


def upgrade0to1000(context):
    """Upgrade from version 0 to version 1000.
    """
    gtool = getToolByName(context, 'portal_groups')

    gtool.addGroup('InclusaoImagens', title='Inclusão de Imagens', roles=['Inclusao de imagens'])
    gtool.addGroup('RevisoresConteudo', title='Revisores de Conteúdo', roles=['Revisor de conteudo'])
    gtool.addGroup('RevisoresConteudo', title='Revisores de Texto', roles=['Revisor de texto'])
    gtool.addGroup('TradutoresTexto', title='Tradutores de texto', roles=['Tradutor de texto'])
