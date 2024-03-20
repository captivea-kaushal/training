{
    'name': 'om_hospital',
    'summary': 'only om_hospital details help of this website',
    'version': '16.0.0.1.0',
    'category': 'library management system',
    'sequence': -100,
    'maintainer': 'Capitivea Software Consulting PVT. LTD.',
    # 'contributors': ["Konsultoo Software Consulting PVT. LTD."],
    # 'description': 'Detailed description of your module',
    'depends': ['base', 'mail', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/patient.tag.csv',
        'data/sequence_data.xml',
        # 'data/patient_tag_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/appointment.xml',
        'views/patient_tag.xml',
        # 'reports/report.xml',
        # 'reports/report_template.xml',
        # 'reports/task2_report.xml',
        # 'reports/task3_report.xml',
        # 'reports/task4_report.xml',
        # 'reports/task5_report.xml'
        # 'security/security_access_data.xml'

    ],
    'demo': [
        'data/patient_tag_data.xml',
        # 'demo/account_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
