from odoo import models,api,fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_get_products(self):
        print('This is Action Get Products')
    #
    #     sale_order_lines = self.env['sale.order.line'].search([
    #         ('order_id.state', 'in', ['draft', 'cancel'])  # Filter by state 'draft' or 'cancel'
    #     ])
    #
    #     for record in self:
    #         return sale_order_lines
