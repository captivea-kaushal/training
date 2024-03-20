from odoo import api, models, fields


class mysaledata(models.Model):
    _name = 'my.saledata'
    _description = "my sale data"
    _inherit = 'hospital.patient'

    hos_owner_name = fields.Char(string="Hospital owner name")

















