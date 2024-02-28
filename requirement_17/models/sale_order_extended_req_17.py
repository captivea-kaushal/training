from odoo import models,api,fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_get_products(self):
        print('This is Action Get Products')

        action = {
            'name': 'Sale Order Lines',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.line',
            'view_mode': 'tree',
            'view_id': False,
            'domain': [('order_id', '!=', False), ('order_id.state', 'in', ['draft', 'sent', 'sale'])],
            'target': 'current',
        }

        view_id = self.env.ref('requirement_17.sale_order_line_req_17__tree_view')
        if view_id:
            action['view_id'] = view_id.id

        print('action : ',action)
        print('view_id :',view_id)

        return action