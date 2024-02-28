{
    'name': 'requirement_17',
    'summary': 'only requirement_15 details help of this website',
    'version': '16.0.0.1.0',
    'category': 'requirement_15 data',
    'maintainer': 'Capitivea Software Consulting PVT. LTD.',
    'sequence': 1,
    'description': 'Detailed description of your module',
    'depends': ['base', 'sale'],
    # 'depends': ['base', 'Hospital', 'sale'],
    'data': [
        'views/sale_order_views.xml',
        # 'security/ir.model.access.csv',
    ],
    'demo': [
        # 'data/demo_sale_order.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
