from odoo import fields,api,models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_all_picking_completed = fields.Boolean(string='All Picking Completed',compute='_compute_picking_confirmation',default=False)

    @api.depends('picking_ids.state')
    def _compute_picking_confirmation(self):
        for order in self:
            if order.picking_ids:
                if any(picking.state in ['draft', 'waiting', 'confirmed', 'assigned'] for picking in order.picking_ids):
                    order.is_all_picking_completed = False
                else:
                    order.is_all_picking_completed = True
            else:
                order.is_all_picking_completed = False