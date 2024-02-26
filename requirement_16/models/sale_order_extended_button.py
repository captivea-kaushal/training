from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_manage_deposits(self):
        for order in self:
            for line in order.order_line.filtered(lambda l: l.product_id and l.product_id.product_tmpl_id.deposit_product_id):
                print('Line : --------->',line)
                deposit_product = line.product_id.product_tmpl_id.deposit_product_id

                deposit_line = order.order_line.filtered(lambda dl: dl.product_id == deposit_product)

                if deposit_line:
                    deposit_line.product_uom_qty = line.product_uom_qty * line.product_id.product_tmpl_id.deposit_product_qty
                else:
                    deposit_line = self.env['sale.order.line'].create({
                        'order_id': order.id,
                        'product_id': deposit_product.id,
                        'product_uom_qty': line.product_uom_qty * line.product_id.product_tmpl_id.deposit_product_qty,
                        'product_uom': line.product_uom.id,
                        'price_unit': deposit_product.lst_price,
                    })

    @api.model_create_multi
    def create(self, values):
        order = super(SaleOrder, self).create(values)
        order.action_manage_deposits()
        return order

    def write(self, values):
        res = super(SaleOrder, self).write(values)
        self.action_manage_deposits()
        return res

    def unlink(self):
        deposit_lines = self.order_line.filtered(lambda l: l.product_id and l.product_id.product_tmpl_id.deposit_product_id)
        deposit_lines.unlink()

        deposit_product_lines = self.order_line.filtered(lambda l: l.product_id and l.product_id.product_tmpl_id.deposit_product_id)
        deposit_product_lines.unlink()

        return super(SaleOrder, self).unlink()