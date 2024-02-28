from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Saleorderinherit(models.Model):
    _inherit = 'sale.order'

    def Manage_Deposits(self):
        for rec in self.order_line:
            product = rec.product_id
            deposit_product = self.find_deposit_product(product)

            if deposit_product:
                # Check if deposit product already added
                if not self.deposit_product_added(deposit_product):
                    self.add_deposit_to_order(deposit_product)
            # if rec.order_line and rec.order_line.product_id and rec.order_line.product_id.deposit_product_id:
            #     pass
        return

    def find_deposit_product(self, product):
        if product.deposit_product_id:
            return product.deposit_product_id

        # Your logic to find the deposit product associated with a regular product
        # This could be querying a database, checking a mapping, etc.
        # return deposit_product

    def deposit_product_added(self, deposit_product):
        if deposit_product.id in self.order_line.product_id.ids:
            return True
        return False

    def add_deposit_to_order(self, deposit_product):
        self.write({'order_line': [(0, 0, {'product_id': deposit_product.id, 'product_uom_qty': 1,
                                           'price_unit': deposit_product.list_price, })]})


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def unlink(self):
        # Call super method to perform the actual deletion
        # for rec in self:
        if self.product_id and self.product_id.deposit_product_id:
            sale_order_line = self.search([('product_id', '=', self.product_id.deposit_product_id.id)])
            if sale_order_line:
                sale_order_line.unlink()
        res = super(SaleOrderLine, self).unlink()
        return res


class ProductproductInherit(models.Model):
    _inherit = 'product.product'
    # _inherit = 'product.template'

    deposit_product_id = fields.Many2one('product.product', string="product_product_id")
    deposit_product_qty = fields.Float(string="deposit product qty", compute='_compute_update_deposit_product_qty',
                                       readonly=False)

    def _compute_update_deposit_product_qty(self):
        for rec in self:
            if rec.free_qty > 1 and rec.deposit_product_qty:
                rec.deposit_product_qty = rec.free_qty
