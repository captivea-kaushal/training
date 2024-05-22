from odoo import models,fields,api

class StudentResult(models.Model):
    _name = 'practice.student.result'
    _description = 'Result of Each Student'
    _rec_name = 'subject'

    subject = fields.Char(string='Subject')
    min_marks = fields.Integer(string='Minimum marks')
    max_marks = fields.Integer(string='Maximum marks')
    obtained_marks = fields.Integer(string='Obtained Marks')

    student_id = fields.Many2one('practice.student.profile',string='Student ID')

    # property_field_new = fields.Properties('New Properties', definition='student_id.student_property_definition',copy=True)