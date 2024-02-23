{
    'name': 'Sale Order Extended',
    'description': 'To extend functionlity of existing sale order',
    'version': '1.0.0',
    'author': 'Karan',
    'sequence': -8,
    'category': 'Practice Exercise',
    'depends': ['base', 'sale', 'crm','sales_team','sale_crm'],
    'data': [
        'views/sale_order_extended.xml',
    ],
    'demo': ['data/demo_crm_tag.xml', ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
