# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name':'Library Books',
    'discription':'This module is made for practicing Controllers',
    'summary':'For practice',
    'version':'1.0.0',
    'sequence':-5,
    'author':'Karan',
    'category':'Portal',
    'depends':['base','website','portal'],
    'data':['security/groups.xml',
            'security/ir.model.access.csv',
            'views/portal_template.xml',
            'views/library_book_view.xml',
            'views/library_user_view.xml',
            ],
    'demo':[],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}