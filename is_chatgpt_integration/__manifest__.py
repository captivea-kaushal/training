# -*- coding: utf-8 -*-
{
    'name': 'Odoo ChatGPT Integration',
    'sequence':-1,
    'version': '16.0.1.1.2',
    'license': 'LGPL-3',
    'summary': 'Odoo ChatGPT Integration',
    'description': 'Allows the application to leverage the capabilities of the GPT language model to generate human-like responses, providing a more natural and intuitive user experience',
    'author': 'InTechual Solutions',
    'website': 'https://intechualsolutions.com',
    'depends': ['base', 'base_setup', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/chatgpt_model_data.xml',
        'data/mail_channel_data.xml',
        'data/user_partner_data.xml',
        'views/res_config_settings_views.xml',
    ],
    'external_dependencies': {'python': ['openai']},
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'application': True,
}
