from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def scan_order_lines_and_get_products(self):
        product_names = []
        for order in self:
            for line in order.order_line:
                product_names.append(line.product_id.name)
                for record in product_names:
                    print("product name: ", record)
        # Do something with the product names, such as printing them or returning them as a list
        # for record in self:

        # print(product_names)
        # You can also perform further actions with the product names


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
