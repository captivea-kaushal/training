# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name':'Captivea Billing Authorization',
    'discription':'This module restricts selective products and accounts with partner to access during generating bills',
    'version':'1.0.0',
    'sequence':-1,
    'author':'Karan',
    'category':'Accounting',
    'depends':['base','account','portal','product','account_accountant','mail','contacts'],
    'data':['security/ir.model.access.csv',
            'views/bill_auth_view.xml',],
    'demo':[],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}