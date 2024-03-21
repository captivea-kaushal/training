{
    'name': 'requirement_19',
    'summary': 'only requirement_19 details help of this website',
    'version': '16.0.0.1.0',
    'category': 'requirement_19 data',
    'maintainer': 'Capitivea Software Consulting PVT. LTD.',
    'sequence': 1,
    # 'contributors': ["Konsultoo Software Consulting PVT. LTD."],
    # 'description': 'Detailed description of your module',
    'depends': ['base', 'sale', 'stock', 'sale_stock'],
    # 'depends': ['base', 'Hospital', 'sale'],
    'data': [
        'views/sale_order.xml',
    ],
    'demo': [
        # 'data/demo_sale_order.xml',
    ],
    'installable': True,
    'application': True,
    # 'auto_install': True,
    'license': 'LGPL-3',
}
