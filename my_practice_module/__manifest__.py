# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name':'My Practice Module',
    'description':'This module is made for practicing odoo concepts',
    'summary':'For practice',
    'version':'1.0.0',
    'sequence':-4,
    'author':'Karan',
    'depends':['base','sales_team'],
    'data':['security/security.xml',
            'security/ir.model.access.csv',
            'views/practice_student_cont.xml',
            'views/practice_student_profile_view.xml',
            'views/practice_student_result_view.xml',
            'views/practice_student_teacher.xml',
            ],
    'demo':[],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}