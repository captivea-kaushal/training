{
    'name': 'Hospital management',
    'summary': 'only patient type Customer help of this website',
    'version': '16.0.0.1.0',
    'category': 'hospital mamangement system',
    'sequence': -100,
    'author': 'Konsultoo Software Consulting PVT. LTD.',
    'maintainer': 'Konsultoo Software Consulting PVT. LTD.',
    'contributors': ["Konsultoo Software Consulting PVT. LTD."],
    'application': True,
    'website': 'https://www.konsultoo.com/',
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/owner.xml'

        # 'views/sale_order_view.xml',
        # 'views/subham_hospital_view.xml'



    ],
    'depends': ['base','sale_management'],
    'license': 'LGPL-3'
}
