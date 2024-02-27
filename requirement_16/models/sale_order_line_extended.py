from odoo import api, fields, models

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def unlink(self):
        print('before deposit line unlink check')
        deposit_lines = self.filtered(lambda line: line.product_id.deposit_product_id)


        print('after deposite line unlink check')

        print('deposit line',deposit_lines)

        if deposit_lines:
            deposit_line_ids = deposit_lines.mapped('product_id.deposit_product_id.id')
            related_order_lines = self.search([('product_id.id', 'in', deposit_line_ids)])
            related_order_lines.unlink()

        res = super(SaleOrderLine, self).unlink()

        return res