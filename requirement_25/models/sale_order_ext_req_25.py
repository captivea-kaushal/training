from odoo import fields, api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_profit_value = fields.Float(string='Total Profit Value', compute='_compute_total_profit_value', store=True)
    total_profit_margin_percentage = fields.Float(string='Total Profit Margin Percentage',
                                                  compute='_compute_total_profit_margin_percentage', store=True)

    @api.depends('order_line.profit_value', 'order_line.price_subtotal', 'order_line.product_uom_qty')
    def _compute_total_profit_value(self):
        for record in self:
            total_profit_value = sum(line.profit_value for line in record.order_line)
            record.total_profit_value = total_profit_value

    @api.depends('order_line.profit_margin_percentage', 'order_line.price_subtotal', 'order_line.product_uom_qty')
    def _compute_total_profit_margin_percentage(self):
        for record in self:
            total_profit_value = sum(line.profit_value for line in record.order_line)
            total_price_subtotal = sum(line.price_subtotal for line in record.order_line)
            total_product_uom_qty = sum(line.product_uom_qty for line in record.order_line)

            if total_price_subtotal != 0 and total_product_uom_qty != 0:
                record.total_profit_margin_percentage = ((total_profit_value / (total_price_subtotal / total_product_uom_qty)) * 100) / total_product_uom_qty
            else:
                record.total_profit_margin_percentage = 0.0
