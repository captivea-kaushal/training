from odoo import models,api,fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        for order in self:
            lines_by_warehouse = {}

            for line in order.order_line:
                warehouse = line.warehouse_id or order.warehouse_id
                if warehouse:
                    if warehouse not in lines_by_warehouse:
                        lines_by_warehouse[warehouse] = self.env['sale.order.line']
                    lines_by_warehouse[warehouse] += line

            for warehouse, lines in lines_by_warehouse.items():
                if warehouse:
                    delivery_order_vals = {
                        'origin': order.name,
                        'partner_id': order.partner_shipping_id.id,
                        'location_dest_id': warehouse.lot_stock_id.id,
                        'location_id': lines.order_id.partner_id.property_stock_customer.id,
                        'picking_type_id':warehouse.pick_type_id.id
                    }

                    delivery_order = order.env['stock.picking'].create(delivery_order_vals)

                    for line in lines:
                        move_vals = {
                            'name': line.name,
                            'product_id': line.product_id.id,
                            'product_uom_qty': line.product_uom_qty,
                            'product_uom': line.product_uom.id,
                            'picking_id': delivery_order.id,
                            'location_id': order.partner_id.property_stock_customer.id,
                            'location_dest_id': warehouse.lot_stock_id.id,

                        }
                        order.env['stock.move'].create(move_vals)
        return res