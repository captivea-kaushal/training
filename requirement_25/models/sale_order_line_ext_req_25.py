from odoo import fields,api,models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    profit_value = fields.Float(string='Profit Value',compute='_compute_profit_value',store=True)
    profit_margin_percentage = fields.Float(string='Profit Margin Percentage',compute='_compute_profit_margin_percentage',store=True)

    @api.depends('product_id.standard_price', 'price_subtotal', 'product_uom_qty')
    def _compute_profit_value(self):
        for line in self:
            line.profit_value = line.price_subtotal - (line.product_id.standard_price*line.product_uom_qty)

    @api.depends('price_subtotal', 'profit_value', 'product_uom_qty')
    def _compute_profit_margin_percentage(self):
        for line in self:
            if line.price_subtotal != 0 and line.product_uom_qty != 0:
                line.profit_margin_percentage = ((line.profit_value / (
                            line.price_subtotal / line.product_uom_qty)) * 100) / line.product_uom_qty
            else:
                line.profit_margin_percentage = 0.0
