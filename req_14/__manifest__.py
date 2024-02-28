{
    'name': 'sale_order_extended',
    'summary': 'only sale_order_extended details help of this website',
    'version': '16.0.0.1.0',
    'category': 'sale_order_extended data',
    'maintainer': 'Capitivea Software Consulting PVT. LTD.',
    'sequence': 1,
    # 'contributors': ["Konsultoo Software Consulting PVT. LTD."],
    # 'description': 'Detailed description of your module',
    'depends': ['base', 'sale', 'crm', 'Hospital'],
    # 'depends': ['base', 'Hospital', 'sale'],
    'data': [
        # 'views/sale.xml',
        # 'security/ir.model.access.csv',
        # 'views/mysaleorder_views.xml'
    ],
    'demo': [
        'data/sale_inherit_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
