{
    'name': 'sale_order_line_multi_warehouse',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'Set warehouses per sale order lines.',
    'sequence': 4,
    'description': """This module will help to set warehouses per sale order 
                      lines and the picking will be created for the selected 
                      warehouses separately.""",
    'author': 'konsultoo Solutions',
    'company': 'konsultoo Solutions',
    'maintainer': 'konsultoo Solutions',
    'website': "https://www.konsultoo.com",
    'depends': ['base', 'sale_management', 'account', 'stock'],
    'data': [
        'views/sale_order_view.xml',
    ],

    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
