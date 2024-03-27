from odoo import models,fields,api,_

class EmployeeExpanse(models.Model):
    _name = 'employee.expanse'
    _description = 'Expense'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def _default_employee_id(self):
        employee = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)], limit=1)
        return employee.id

    name = fields.Char(string='Name',required=True)
    state = fields.Selection([('draft', 'Draft'), ('inprogress', 'In Progress'), ('done', 'Done'), ('cancel', 'Cancelled')], default='draft')
    employee_id = fields.Many2one('hr.employee', compute='_compute_employee_id', string="Employee",
                                  store=True, readonly=False, tracking=True,
                                  state={'approved': [('readonly', True)], 'done': [('readonly', True)]},
                                  default=_default_employee_id,
                                  check_company=True)
    expense_type = fields.Selection([('domestic', 'Domestic'), ('international', 'International')],string='Expense Type',)
    attachment = fields.Binary(string='Attachment')
    amount = fields.Float(string='Amount', tracking=True,required=True)
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
                                 state={'draft': [('readonly', False)], 'cancel': [('readonly', False)]},
                                 default=lambda self: self.env.company)

    @api.depends('company_id')
    def _compute_employee_id(self):
        if not self.env.context.get('default_employee_id'):
            for expense in self:
                expense.employee_id = self.env.user.with_company(expense.company_id).employee_id


    def action_confirm(self):
        self.state = 'inprogress'
        self.message_post(body=_("Expense confirmed."), subtype_id=self.env.ref('mail.mt_note').id)

    def action_approve(self):
        self.state = 'done'
        self.message_post(body=_("Expense approved."), subtype_id=self.env.ref('mail.mt_note').id)

    def action_cancel(self):
        self.state = 'cancel'
        self.message_post(body=_("Expense cancelled."), subtype_id=self.env.ref('mail.mt_note').id)

    def action_set_to_draft(self):
        self.state = 'draft'