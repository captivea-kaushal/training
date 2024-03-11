from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    history_unit_price = fields.Float(string='History Unit Price',compute="_compute_history_unit_price",readonly=True,store=True)
    is_compute_executed = fields.Boolean(string='Compute Executed', default=False)

    @api.depends('order_id.partner_id', 'product_id', 'is_compute_executed')
    def _compute_history_unit_price(self):
        for record in self:
            if record.order_id and record.product_id and not record.is_compute_executed:
                last_confirmed_order_line = self.env['purchase.order.line'].search([
                    ('order_id.state', '=', 'purchase'),
                    ('order_id.partner_id', '=', record.order_id.partner_id.id),
                    ('product_id', '=', record.product_id.id),
                ], limit=1)

                if last_confirmed_order_line:
                    record.history_unit_price = last_confirmed_order_line.price_unit
                else:
                    record.history_unit_price = 0.0

                record.is_compute_executed = True
            else:
                record.history_unit_price = 0.0