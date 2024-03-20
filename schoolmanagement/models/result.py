from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


# from odoo.exceptions import UserError


class StudentClass(models.Model):
    _name = 'result.student'
    _description = 'school.student_details'
    _rec_name = "result_id"

    # subject_marks = fields.Integer()
    sub_code = fields.Char()
    min_marks = fields.Integer(default=30)
    max_marks = fields.Integer(default=100)
    marks_obtained = fields.Integer()
    result_status = fields.Selection([('pass', 'Pass'), ('fail', 'Fail')], compute='_compute_marks_obtained')

    subject_id = fields.Many2one(comodel_name='student.subject', string="SUBJECT NAME")

    result_id = fields.Many2one(comodel_name='student.school', string='RESULT')

    # amount_total = fields.Monetary(string="Total", store=True, compute='_compute_amounts', tracking=4)

    _sql_constraints = [
        ('result_uniq', 'unique (result_id,subject_id)',
         'The subject and result  of  every student must be unique.!')
    ]

    @api.depends('marks_obtained')
    def _compute_marks_obtained(self):
        for record in self:
            # record.marks_obtained = record.subject_marks
            if record.marks_obtained > record.min_marks and record.marks_obtained <= record.max_marks:
                record.result_status = 'pass'
            else:
                record.result_status = 'fail'

    _sql_constraints = [
        ('result_uniq', 'unique (result_id)',
         'The name of the country must be unique !')
    ]

    # @api.constrains('subject_marks')
    # def raise_error(self):
    #     if self.subject_marks > 100 or self.subject_marks < 30:
    #         raise ValidationError(_('You can select either a format or a specific page width/height, but not both.'))
