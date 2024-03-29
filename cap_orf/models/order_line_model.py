from odoo import fields,models,api


class OrderLine(models.Model):
    _name = 'order.line'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product',string='Product')
    product_image = fields.Binary(string='Image')
    quantity = fields.Float('Quantity',default='1')
    uom_id = fields.Many2one('uom.uom',string='UoM')
    unit_price = fields.Monetary('Unit Price')
    currency_id=fields.Many2one('res.currency',string='Currency')
    subtotal = fields.Monetary(currency_field='currency_id',string='Subtotal')
    purchase_orf_id = fields.Many2one('purchase.orf',string='Purchase ORF')

    @api.onchange('product_id')
    def _onchange_product_image(self):
        if self.product_id:
            self.product_image = self.product_id.image_1920

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.unit_price = self.product_id.lst_price

    @api.onchange('unit_price','quantity')
    def calculate_subtotal(self):
        if self.unit_price:
            self.subtotal = self.unit_price * self.quantity

    @api.onchange('product_id')
    def calculate_uom_id(self):
        if self.product_id:
            self.uom_id = self.product_id.uom_id.id
        #
        #
        # defaults = super(OrderLine, self).default_get(fields_list)
        # # Set default uom_id and currency_id based on product_id
        # if 'product_id' in fields_list:
        #     product = self.env['product.product'].browse(defaults.get('product_id'))
        #     defaults['uom_id'] = product.uom_id.id if product.uom_id else False
        #     defaults['currency_id'] = product.company_id.currency_id.id if product.company_id.currency_id else False
        # return defaults

