# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name':'CAP_ORF',
    'discription':'This module is made for practicing odoo',
    'version':'1.0.0',
    'sequence':1,
    'author':'Karan',
    'category':'Purchase',
    'depends':['base','purchase','portal','product','stock','mail','website'],
    'data':['security/ir.model.access.csv',
            'data/orf_sequence.xml',
            'views/purchase_orf_view.xml',
            'views/purchase_order_extended_view.xml',
            'controllers/orf_portal.xml'
            ],
    'demo':[],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}