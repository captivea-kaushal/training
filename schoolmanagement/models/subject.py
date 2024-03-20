from odoo import api, models, fields


class StudentClass(models.Model):
    _name = 'student.subject'
    _description = 'school.subject_details'
    _rec_name = 'subject_name'

    subject_name = fields.Char(string="enter subject name: ")
