from odoo import fields,models,api

class UserSale(models.Model):
    _inherit = 'res.users'

    sale_order_ids = fields.One2many('sale.order','user_id',string="sales persons")