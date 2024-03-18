from odoo import api, fields, models


class stock_class(models.Model):
    _inherit = 'stock.picking'
