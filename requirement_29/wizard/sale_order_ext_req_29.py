from odoo import api, fields, models


class SaleOrder(models.TransientModel):
    _name = 'sale.salesperson'
    _transient_max_count = 3
    _transient_max_hours = 0.1

    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')
    sales_person = fields.Many2many('res.users', string="Sales Person")

    def action_print_report(self):
        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
            'sales_person': self.sales_person.ids,
        }
        return self.env.ref('requirement_29.action_report_sale_order_req_29').report_action(self, data=data)
















            # context = {'view_mode': 'form',
            #            'view_id': self.env.ref('requirement_29.action_report_sale_order_req_29').id,
            #            'res_model': 'sale.order',
            #            'res_id': record.id,
            #            }
            # return {
            #     'context':context,
            #     'name': 'Sales by Salesperson',
            #     'type': 'ir.actions.report',
            #     # 'res_model': 'sale.order',
            #     # 'view_mode': 'form',
            #     # 'view_id': self.env.ref('requirement_29.report_sale_order_req_29_template').id,
            #     # 'res_id': record.id,
            #     'target': 'self', }


