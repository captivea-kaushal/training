from odoo import fields,api,models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm_and_validate(self):

        self.action_confirm()
        self.action_view_delivery()

        if self.picking_ids:
            for picking in self.picking_ids:
                for move in picking.move_ids:
                    move.quantity_done = move.product_uom_qty

                picking.button_validate()

                return {
                            'name': 'Stock Picking',
                            'type': 'ir.actions.act_window',
                            'res_model': 'stock.picking',
                            'view_mode': 'form',
                            'view_id': self.env.ref('stock.view_picking_form').id,
                            'res_id': picking.id,
                            'target': 'main', }