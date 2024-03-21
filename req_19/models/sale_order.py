from odoo import models, fields, api


class stock_picking(models.Model):
    _inherit = 'stock.picking'


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_picking_completed = fields.Boolean(string='picking completed',
                                          compute='_custom_compute', default=False)

    @api.depends('picking_ids.state')
    def _custom_compute(self):
        for order_lines in self:
            if order_lines.picking_ids:
                if any(picking.state in ['draft', 'waiting', 'confirmed', 'assigned'] for picking in
                       order_lines.picking_ids):
                    order_lines.is_picking_completed = False
                else:
                    order_lines.is_picking_completed = True
            else:
                order_lines.is_picking_completed = False


# Model
#
# sale.order
#
# Fields
#
# is_all_picking_completed - Boolean - Compute - Store - False
#
# This field should be able to search whether all the related pickings(Delivery orders) are validated or not.
# If any one of the picking is not validated then this field should not be set to True, in case all the pickings are validated then
# it should be marked as True. Any picking is cancelled, that should also be considered as completed.
# In summary any picking in draft, waiting, partial available state should return False
#
#
# View
#
# Inherit search view and perform the above operation
#
# Add is_all_picking_completed Filter to search view
