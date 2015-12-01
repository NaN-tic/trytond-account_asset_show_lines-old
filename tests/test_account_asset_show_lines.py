# This file is part of the account_asset_show_lines module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AccountAssetShowLinesTestCase(ModuleTestCase):
    'Test Account Asset Show Lines module'
    module = 'account_asset_show_lines'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountAssetShowLinesTestCase))
    return suite