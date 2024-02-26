from odoo import api,fields,models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    deposit_product_id = fields.Many2one('product.product',string='Deposit Product',ondelete='cascade')
    deposit_product_qty = fields.Integer(string='Deposit Product Qty')
