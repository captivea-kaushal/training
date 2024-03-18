from odoo import api, fields, models


class Stock_picking(models.Model):
    _inherit = 'stock.picking'


    def fun(self, vals):
        print("product_uom", self.product_uom_qty)

        # for rec in self:
        #     print("product_uom", self.product_uom_qty)


#

# from odoo import models, fields, api


# class StockPicking(models.Model):
#     _inherit = 'stock.picking'
#
#     value = fields.Float(string='Value', compute='_compute_value', store=True)
#
#     @api.depends('move_lines.product_uom_qty', 'move_lines.product_id.standard_price')
#     def _compute_value(self):
#         for picking in self:
#             value = 0.0
#             for move in picking.move_lines:
#                 value += move.product_uom_qty * move.product_id.standard_price
#             picking.value = value


# class StockPickingReport(models.AbstractModel):
#     # _name = 'report.your_module.stock_picking_report_template'
#     # _description = 'Stock Picking Report'
#     _inherit = 'stock.picking'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         # Retrieve stock picking data
#         stock_picking_records = self.env['stock.picking'].browse(docids)
#         print("stock_picking_records", stock_picking_records)
#
#         # Initialize dictionary to store product counts
#         product_counts = {}
#
#         # Loop through each stock picking record
#         for picking in stock_picking_records:
#             # Loop through each move in the picking
#             for move in picking.move_lines:
#                 # Retrieve product ID and quantity
#                 product_id = move.product_id
#                 quantity = move.product_qty
#                 print("quantity", quantity)
#                 print("product_id", product_id)
#                 # Update product counts dictionary
#                 if product_id in product_counts:
#                     product_counts[product_id] += quantity
#                 else:
#                     product_counts[product_id] = quantity
#
#         # Prepare data for report template
#         report_data = {
#             'stock_picking_records': stock_picking_records,
#             'product_counts': product_counts,
#         }
#         print("report data...", report_data)
#         return report_data

class account_move(models.Model):
    _inherit = 'account.move'
