from odoo import api, models, fields


class StudentClass(models.Model):
    _name = 'library.teacher'
    _description = 'library teacher  details '
    _rec_name = 'teacher_name'

    teacher_id = fields.Char(string="Teacher id")
    teacher_name = fields.Char(string=" Teacher Name: ")
    department = fields.Char(string="teacher department")
    gender = fields.Selection([('f_male1', 'Female'), ('m_male1', 'male'), ('transgender1', 'Transgender')],
                              string="Gender: ")

    student_rec_ids = fields.One2many('library.student', 'teacher_rel_id', string='student record')
