from odoo import models,api,fields

class SaleOrderExtended15(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):

        result = super(SaleOrderExtended15, self).action_confirm()
        delivery_line = self.order_line.filtered(lambda x: x.is_delivery)
        if not delivery_line:
            custom_product = self.env.ref('requirement_15.product_delivery_extended')
            self.order_line.create({
                'order_id': self.id,
                'product_id': custom_product.id,
                'product_uom_qty': 1.0,
                'price_unit': custom_product.list_price,
                'is_delivery': True,
            })

        return result