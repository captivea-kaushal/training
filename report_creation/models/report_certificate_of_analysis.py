from odoo import models,fields,api


class SaleOrderReport(models.Model):
    _inherit = 'sale.order'