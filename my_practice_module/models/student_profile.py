from odoo import fields, models, api


class StudentProfile(models.Model):
    _name = 'practice.student.profile'
    _description = 'Details of student'
    _rec_name = 'student_name'

    student_name = fields.Char(string='Name', default='Please Enter your name here', required=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Float(string='Age')
    counter = fields.Integer(string='ref count')
    scale1 = fields.Integer(string='Scale1')

    base_count = fields.Integer(string='Base Count')

    high_name = fields.Char('High onchange',compute="_compute_name",readonly=False,store=True)

    # student_property_definition = fields.PropertiesDefinition('Student Properties')


    def _compute_name(self):
        for rec in self:
            rec.high_name = rec.student_name