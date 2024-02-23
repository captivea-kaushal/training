# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Report Creations',
    'version' : '1.0.0',
    'author':'karan',
    'summary': 'various report creation',
    'sequence': -1,
    'description': 'for creating various types of reports',
    'category': 'practice',
    'depends' : ['base','sale'],
    'data': ['security/ir.model.access.csv',
             'report/batch_production_report.xml',
             'report/certificate_of_analysis_report.xml',
             'report/certificate_of_origin_report.xml',
             'report/commercial_invoice_report.xml',
             'report/packing_list_report.xml',
             'views/report_details_view.xml',],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}