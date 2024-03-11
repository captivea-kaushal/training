from odoo import fields, models, api
from datetime import datetime


class SalebySalesperson(models.AbstractModel):
    _name = 'report.requirement_29.report_sale_order_req_29_template'
    _description = 'Report sales by salesperson'

    def _get_report_values(self, docids, data=None):

        from_date = datetime.strptime(data.get('from_date'), '%Y-%m-%d').date()
        to_date = datetime.strptime(data.get('to_date'), '%Y-%m-%d').date()
        sales_person_ids = data.get('sales_person')

        print('from_date ',from_date)
        print('to_date ',to_date)
        print('sales_person_ids : ',sales_person_ids)


        domain = [('create_date', '>=', from_date), ('create_date', '<=', to_date)]

        print('domain :',domain)
        if sales_person_ids:
            domain.append(('user_id', 'in', sales_person_ids))



        docs = self.env['sale.order'].search(domain)

        print('docs :',docs)

        return {
            'doc_ids': docids,
            'doc_model': self.env['sale.order'],
            'data': data,
            'docs': docs,
            'from_date_k':from_date,
            'to_date_k':to_date,
        }