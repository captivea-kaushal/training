from odoo import fields, models

class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    warehouse_id = fields.Many2one('stock.warehouse',store=True,string='Warehouse',readonly=False)

