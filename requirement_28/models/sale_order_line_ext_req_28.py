from odoo import fields, models

class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

