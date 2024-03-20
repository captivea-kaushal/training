from odoo import api, fields, models


class Hospital_Owner(models.Model):
    _name = 'hospital.owner'
    _description = 'hospital.owner_records'
    # _inherit = 'sale.order'
    # _rec_nmae = 'dob'
    # _auto = False

    owner_name = fields.Char(string=" Owner Name")
