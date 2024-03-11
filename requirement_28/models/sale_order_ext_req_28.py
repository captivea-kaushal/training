from odoo import models,api,fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'