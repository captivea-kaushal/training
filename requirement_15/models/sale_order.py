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

#
# xml का उपयोग करके एक उत्पाद बनाएं
#
# Sale.order फ़ॉर्म पर पुष्टि बटन पर, शिपिंग उत्पाद स्वचालित रूप से sales.order.line मॉडल में जोड़ा जाना चाहिए
#
# Sale.order मॉडल के ऑर्डर पुष्टिकरण की उचित विधि प्राप्त करें और शिपिंग लाइन को स्वचालित रूप से जोड़ने के लिए तर्क जोड़ें
#
# सुनिश्चित करें कि शिपिंग लाइन केवल एक बार जोड़ी जानी चाहिए - sales.order.line मॉडल में "is_delivery" फ़ील्ड का उपयोग करने का प्रयास करें
