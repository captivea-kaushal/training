from odoo import models,fields,api

class StudentResult(models.Model):
    _name = 'practice.student.result'
    _description = 'Result of Each Student'

    subject = fields.Char(string='Subject')
    min_marks = fields.Integer(string='Minimum marks')
    max_marks = fields.Integer(string='Maximum marks')
    obtained_marks = fields.Integer(string='Obtained Marks')

    student_profile_id = fields.Many2one('practice.student.profile', string='Student Profile', required=True)