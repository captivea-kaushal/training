from odoo import models,fields,api,_


class BillAuth(models.Model):
    _name = 'bill.auth'
    _description = 'Billing Authorization Parameters'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    allowed_product_ids = fields.Many2many('product.product',string='Allowed Products',required=True)
    allowed_account_ids = fields.Many2many('account.account',string='Allowed Accounts',required=True)