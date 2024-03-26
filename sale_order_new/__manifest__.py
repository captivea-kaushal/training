# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Order New',
    'version': '1.0.0',
    'sequence': -2,
    'summary': 'Wizard',
    'author': 'Karan',
    'depends': ['base', 'sale', 'sale_management'],
    'data': ['security/ir.model.access.csv',
             'views/sale_order.xml',
             'wizard/sale_order_wizard_view.xml',
             ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'sale_order_new/static/src/js/tree_button.js',
            'sale_order_new/static/src/xml/tree_button.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
