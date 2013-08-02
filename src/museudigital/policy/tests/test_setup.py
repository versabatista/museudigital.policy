# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from museudigital.policy.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of museudigital.policy into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if museudigital.policy is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('museudigital.policy'))

    def test_uninstall(self):
        """Test if museudigital.policy is cleanly uninstalled."""
        self.installer.uninstallProducts(['museudigital.policy'])
        self.assertFalse(self.installer.isProductInstalled('museudigital.policy'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IMuseudigitalPolicyLayer is registered."""
        from museudigital.policy.interfaces import IMuseudigitalPolicyLayer
        from plone.browserlayer import utils
        self.failUnless(IMuseudigitalPolicyLayer in utils.registered_layers())
