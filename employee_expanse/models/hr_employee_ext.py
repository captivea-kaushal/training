from odoo import api, fields, models, _


class HrEmployeePrivate(models.Model):

    _inherit = "hr.employee"

    expense_ids = fields.One2many('employee.expanse','employee_id',string='Expanses')

    def action_new_smart_button(self):
        self.ensure_one()
        return {
            'name': _("Related Expanses"),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'employee.expanse',
            'domain': [('id', 'in', self.expense_ids.ids)]
        }