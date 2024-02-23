from odoo import fields, models, api
from datetime import datetime, timedelta
from odoo.osv import expression


class StudentTeacher(models.Model):
    _name = 'practice.student.teacher'
    _description = 'Details of Teacher'

    teacher_name = fields.Char(string='Teacher Name')

    subject = fields.Char(string='Subject')
    date_of_joining = fields.Date(string='Date of joining')

    is_active = fields.Boolean(string='Is Active')

    def name_get(self):
        res = []
        for rec in self:
            teacher_name = rec.teacher_name or ''
            subject = rec.subject or ''
            name = f"{teacher_name} - {subject}"
            res.append((rec.id, name))
        return res

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if args is None:
            args = []
        domain = ['|', ('teacher_name', operator, name), ('subject', operator, name)]
        return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
