from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_manage_deposits(self):
        for order in self:
            deposit_lines = {}

            for line in order.order_line.filtered(lambda x: x.product_id and x.product_id.product_tmpl_id.deposit_product_id):
                deposit_product = line.product_id.product_tmpl_id.deposit_product_id
                deposit_qty = line.product_uom_qty * line.product_id.product_tmpl_id.deposit_product_qty

                if deposit_product in deposit_lines:
                    deposit_lines[deposit_product] += deposit_qty
                else:
                    deposit_lines[deposit_product] = deposit_qty

            for deposit_product, total_qty in deposit_lines.items():
                deposit_line = order.order_line.filtered(lambda x: x.product_id == deposit_product)

                if deposit_line:
                    deposit_line.product_uom_qty = total_qty
                else:
                    deposit_line = self.env['sale.order.line'].create({
                        'order_id': order.id,
                        'product_id': deposit_product.id,
                        'product_uom_qty': total_qty,
                        'product_uom': deposit_product.uom_id.id,
                        'price_unit': deposit_product.lst_price,
                    })

    @api.model_create_multi
    def create(self, values):
        print('before create >>>>>>>>>>>>>')
        order = super(SaleOrder, self).create(values)
        order.action_manage_deposits()
        return order

    def write(self, values):
        print('before write >>>>>>>>>>>>>')
        res = super(SaleOrder, self).write(values)
        self.action_manage_deposits()
        return res