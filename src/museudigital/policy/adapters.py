# encoding: utf-8

from plone.stringinterp.adapters import MailAddressSubstitution


class RevisorTextoEmailSubstitution(MailAddressSubstitution):

    category = u'E-Mail Addresses'
    description = u'Revisores de Texto'

    def safe_call(self):
        return self.getEmailsForRole('Revisor de texto')


class RevisorConteudoEmailSubstitution(MailAddressSubstitution):

    category = u'E-Mail Addresses'
    description = u'Revisores de Conteúdo'

    def safe_call(self):
        return self.getEmailsForRole('Revisor de conteudo')


class TradutorEmailSubstitution(MailAddressSubstitution):

    category = u'E-Mail Addresses'
    description = u'Tradutores de Texto'

    def safe_call(self):
        return self.getEmailsForRole('Tradutor de texto')


class InclusaoImagensEmailSubstitution(MailAddressSubstitution):

    category = u'E-Mail Addresses'
    description = u'Inclusão de Imagens'

    def safe_call(self):
        return self.getEmailsForRole('Inclusao de imagens')
