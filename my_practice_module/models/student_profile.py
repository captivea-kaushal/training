from odoo import fields, models, api
from datetime import datetime, timedelta


class StudentProfile(models.Model):
    _name = 'practice.student.profile'
    _description = 'Details of student'
    _rec_name = 'student_name'

    student_name = fields.Char(string='Name', default='Please Enter your name here', required=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Float(string='Age')
    counter = fields.Integer(string='ref count')
    scale1 = fields.Integer(string='Scale1', compute="_compute_scale_1", inverse="_set_counter")

    result_for_student_ids = fields.One2many('practice.student.result', 'student_profile_id', string='Result')
    teacher_for_student_id = fields.Many2one('practice.student.teacher',string='Teacher')

    base_count = fields.Integer(string='Base Count')
    variable_count = fields.Integer(compute='_compute_dependent_field')

    @api.depends('base_count')
    def _compute_dependent_field(self):
        for record in self:
            record.variable_count = record.base_count * 2

    @api.onchange('base_count')
    def _onchange_base_field(self):
        if self.base_count:
            self.variable_count = self.base_count * 3

    @api.depends('counter')
    def _compute_scale_1(self):
        for record in self:
            record.scale1 = 2 * record.counter

    def _set_counter(self):
        for record in self:
            record.counter = record.scale1 // 2

    # @api.model_create_multi
    def create(self, vals):
        res = super(StudentProfile, self).create(vals)
        result_model = self.env['practice.student.result']
        # for profile in res:
        result_model.create([{'subject': 'Maths',
                                 'min_marks': 35,
                                 'max_marks': 100,
                                 'obtained_marks': 0,
                                 'student_profile_id': res.id, },
                                 {'subject': 'Gujarati',
                                 'min_marks': 35,
                                 'max_marks': 100,
                                 'obtained_marks': 0,
                                 'student_profile_id': res.id, }])

        return res

    def action_test(self):
        for record in self:

            # env.search()

            # students = self.env['practice.student.profile'].sudo().search([])
            # students = self.env['practice.student.profile'].sudo().search([('age','>',15)])
            # students = self.env['practice.student.profile'].sudo().search([],offset=1,limit=3)

            # env.search_count()

            # students = self.env['practice.student.profile'].sudo().search_count([])
            # students = self.env['practice.student.profile'].sudo().search_count([('age','>',15)])
            # students = self.env['practice.student.profile'].sudo().browse(4)
            # if students.exists():
            #     students.write({'counter':3})

            # students = self.env['practice.student.profile'].sudo().browse(4).unlink()

            # students = self.env['practice.student.profile'].sudo().browse(20)
            # students.copy({'counter':3})

            print('>>>>>>>>>>>>>>>')
            print(f'students : {students}')
            print('>>>>>>>>>>>>>>>')