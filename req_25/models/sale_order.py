from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    profit_margin_percentage = fields.Float(string='Profit Margin (%)', compute='_compute_profit_margin', store=True)
    profit_value = fields.Monetary(string='Profit', compute='_compute_profit_value', store=True)

    @api.depends('product_id', 'price_unit', 'product_id.standard_price')
    def _compute_profit_margin(self):
        for line in self:
            if line.product_id.standard_price:
                cost_price = line.product_id.standard_price
                profit = line.price_unit - cost_price
                profit_margin = (profit / cost_price) * 100 if cost_price != 0 else 0
                line.profit_margin_percentage = profit_margin

    @api.depends('product_id', 'price_unit', 'product_id.standard_price')
    def _compute_profit_value(self):
        for line in self:
            if line.product_id.standard_price:
                cost_price = line.product_id.standard_price
                profit = line.price_unit - cost_price
                line.profit_value = profit


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_profit_margin_percentage = fields.Float(string='Total Profit Margin (%)',
                                                  compute='_compute_total_profit_margin', store=True)
    total_profit_value = fields.Monetary(string='Total Profit', compute='_compute_total_profit_value', store=True)

    @api.depends('order_line')
    def _compute_total_profit_margin(self):
        for order in self:
            total_margin_percentage = 0.0
            for line in order.order_line:
                total_margin_percentage += line.profit_margin_percentage
            if order.amount_untaxed != 0:
                order.total_profit_margin_percentage = (total_margin_percentage / len(order.order_line))
            else:
                order.total_profit_margin_percentage = 0.0

    @api.depends('order_line')
    def _compute_total_profit_value(self):
        for order in self:
            total_profit = 0.0
            for line in order.order_line:
                total_profit += line.profit_value
            order.total_profit_value = total_profit
