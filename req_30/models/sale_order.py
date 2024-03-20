from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    my_custom_history = fields.Float(string='history_unit_price', compute="_compute_custom",
                                     store=True)
    is_compute_executed = fields.Boolean(string='custom_compute_executed', default=False)

    @api.depends('order_id.partner_id', 'product_id', 'is_compute_executed')
    def _compute_custom(self):
        for record in self:
            if record.order_id and record.product_id and not record.is_compute_executed:
                my_last_confirmed_order_line = self.env['sale.order.line'].search(
                    [('order_id.state', '=', 'sale'), ('order_id.partner_id', '=', record.order_id.partner_id.id),
                     ('product_id', '=', record.product_id.id)], limit=1)

                record.my_custom_history = my_last_confirmed_order_line.price_unit if my_last_confirmed_order_line else 0.0
                record.is_compute_executed = True
            else:
                record.my_custom_history = 0.0


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    my_custom_history = fields.Float(string='History_Unit_Price', compute='_compute_custom')
    is_compute_executed = fields.Boolean(string='my custom Compute Executed', default=False)

    @api.depends('order_id.partner_id', 'product_id', 'is_compute_executed')
    def _compute_custom(self):
        for record in self:
            if record.order_id and record.product_id and not record.is_compute_executed:
                custom_last_confirmed_order_line = self.env['purchase.order.line'].search(
                    [('order_id.state', '=', 'purchase'), ('order_id.partner_id', '=', record.order_id.partner_id.id),
                     ('product_id', '=', record.product_id.id)], limit=1)

                record.my_custom_history = custom_last_confirmed_order_line.price_unit if custom_last_confirmed_order_line else 0.0
                record.is_compute_executed = True
            else:
                record.my_custom_history = 0.0
