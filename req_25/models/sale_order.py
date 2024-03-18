from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    profit_margin = fields.Float(string='Profit Margin (%)', compute='_compute_profit', store=True)
    profit_value = fields.Float(string='Profit Value', compute='_compute_profit', store=True)

    #
    @api.depends('price_unit', 'product_id.standard_price')
    def _compute_profit(self):
        for line in self:
            cost_price = line.product_id.standard_price
            sale_price = line.price_unit
            profit_value = sale_price - cost_price
            line.profit_value = profit_value
            if cost_price != 0:
                line.profit_margin = (profit_value / cost_price) * 100
            else:
                line.profit_margin = 0


#
#     # @api.model
#     @api.model_create_multi
#     def create(self, values):
#         res = super(SaleOrderLine, self).create(values)
#         res._compute_profit()
#         return res
#
#     def write(self, values):
#         res = super(SaleOrderLine, self).write(values)
#         self._compute_profit()
#         return res


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_profit_margin = fields.Float(string='Total Profit Margin (%)', compute='_compute_total_profit')
    total_profit_value = fields.Float(string='Total Profit Value', compute='_compute_total_profit')

    @api.depends('order_line.profit_margin', 'order_line.profit_value')
    def _compute_total_profit(self):
        for order in self:
            order.total_profit_margin = sum(order.order_line.mapped('profit_margin'))
            order.total_profit_value = sum(order.order_line.mapped('profit_value'))
