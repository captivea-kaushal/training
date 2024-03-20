from odoo import models, fields, api


class StudentDegree(models.Model):
    _name = "student.degree"
    _description = "student.degree.details"
    _rec_name = 'degree_name'

    degree_name = fields.Char(string="student degree")

    _sql_constraints = [
        ('degree_uniq', 'unique (degree_name)', 'The name must be unique !')
    ]
