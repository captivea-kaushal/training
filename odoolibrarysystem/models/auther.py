from odoo import api, models, fields


class AutherClass(models.Model):
    _name = 'library.auther'
    _description = 'auther details '
    _rec_name = 'auther_name'

    auther_name = fields.Char(string=" Auther Name: ")

    _order = 'id desc'
