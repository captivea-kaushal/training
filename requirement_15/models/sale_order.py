from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super().action_confirm()
        shipping_product_id = self.env.ref('requirement_15.product_custom_data')
        # print("shipping_product_id", shipping_product_id)
        for order in self:
            order.write({
                'order_line': [
                    (0, 0, {'order_id': order.id,
                            'product_id': shipping_product_id.id,
                            'product_uom_qty': 1,  # Assuming quantity is 1 for shipping product
                            'price_unit': 1}),
                ]
            })
        return res


class Producttemplate(models.Model):
    _inherit = 'product.product'

    my_product_id = fields.Many2one('product.template', string="my product template id")

