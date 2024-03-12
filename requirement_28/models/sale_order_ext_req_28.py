from odoo import models,api,fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        for order in self:
            for line in order.order_line:
                warehouse_id = line.warehouse_id.id or order.warehouse_id.id

                # Create delivery order for each line
                print('line - ',line)
                picking_vals = {
                    'origin': order.name,
                    'partner_id': order.partner_id.id,
                    'location_dest_id': self.env['stock.warehouse'].browse(warehouse_id).lot_stock_id.id,
                    'location_id': line.order_id.partner_id.property_stock_customer.id,
                    'picking_type_id':self.env['stock.warehouse'].browse(warehouse_id).pick_type_id.id
                    # Add other necessary fields
                }

                print('picking_vals - ',picking_vals)


                picking = self.env['stock.picking'].create(picking_vals)

                print('picking - ', picking)

                # Add order lines to the delivery order
                move_vals = {
                    'name': line.name,
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.product_uom_qty,
                    'product_uom': line.product_uom.id,
                    'picking_id': picking.id,
                    'location_id':line.order_id.partner_id.property_stock_customer.id,
                    'location_dest_id':self.env['stock.warehouse'].browse(warehouse_id).lot_stock_id.id,
                    # Add other necessary fields
                }

                print('move_vals - ', move_vals)

                self.env['stock.move'].create(move_vals)

        return res