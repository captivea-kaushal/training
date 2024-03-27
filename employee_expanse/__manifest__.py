# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Expenses',
    'version': '1.0.0',
    'category': 'Human Resources',
    'sequence': -1,
    'summary': 'Manages Domestic and international expanses of employees',
    'author':'Karan',
    'description': """
Manage Domestic and International expenses by Employees
============================

This application allows you to manage your employees' domestic and international expenses. It gives you access to your employees’ expanses and give you the right to approve and validate or cancel the expanses.
Employee can encode their own expenses.


The whole flow is implemented as:
---------------------------------
* Draft expense
* Submitted by the employee to his manager
* Approved by his manager
* final approval by the admin
    """,
    'depends': ['base','hr','mail'],
    'data': ['security/groups.xml',
            'security/ir.model.access.csv',
             'views/employee_expanse_view.xml',
             'views/hr_employee.xml',
             ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
