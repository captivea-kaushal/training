from odoo import api, fields, models


class SaleOrder(models.TransientModel):
    _name = 'sale.button'
    _transient_max_count = 3
    _transient_max_hours = 1.0

    name = fields.Char('Name')