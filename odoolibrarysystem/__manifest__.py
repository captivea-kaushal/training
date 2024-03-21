{
    'name': 'odoolibrarysystem',
    'summary': 'only library details help of this website',
    'version': '16.0.0.1.0',
    'category': 'library management system',
    'sequence': -100,
    'maintainer': 'Capitivea Software Consulting PVT. LTD.',
    # 'contributors': ["Konsultoo Software Consulting PVT. LTD."],
    # 'description': 'Detailed description of your module',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/book.xml',
        'views/subject.xml',
        'views/auther.xml',
        'views/teacher.xml',

        # 'security/security_access_data.xml'

    ],
    'demo': [
        # 'demo/account_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
