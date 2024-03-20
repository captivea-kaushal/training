from odoo import models, fields, api


class StudentDegree(models.Model):
    _name = "student.qualification"
    _description = "student.qualification.details"
    _rec_name = "student_degree_id"

    # college = fields.Char(string="College Name")
    student_degree_id = fields.Many2one("student.degree", string="Student Degree")
    percentage = fields.Float(string="Student Percentage")
    grade = fields.Selection(
        [('First Division', 'First Division'), ('Second Division', 'Second Division'),
         ('Third Division', 'Third Division'), ('Fail', 'Fail'), ],
        string="Grade", compute="_compute_percentage", store=True)
    qualification_relation_id = fields.Many2one('student.school')

    _sql_constraints = [
        ('student_degree_uniq', 'unique(student_degree_id,qualification_relation_id)',
         'The code of the account must be unique per company !')
    ]

    @api.depends('percentage')
    def _compute_percentage(self):
        for record in self:
            if record.percentage >= 60.00 and record.percentage <= 100.00:
                record.grade = 'First Division'
            elif record.percentage >= 40.00 and record.percentage <= 59.00:
                record.grade = 'Second Division'
            elif record.percentage >= 30.00 and record.percentage <= 39.00:
                record.grade = 'Third Division'
            elif record.percentage <= 29.00:
                record.grade = 'Fail'

        # _sql_constraints = [
        #     ('QUALIFICATION_uniq', 'unique (degree_name,qualification_relation_id)',
        #      'The  college name must be unique !')
        # ]
        # _sql_constraints = [
        #     ('percentage_uniq', 'unique (percentage)', 'The  college name and percentage must be unique !')
        # ]
        # _sql_constraints = [
        #     ('Grade_uniq', 'unique (grade)', 'The  college name percentage and grade must be unique !')
        # ]

        # @api.depends('school_student_ids')
        # def _compute_school_student(self):
        #     for record in self:
        #         record.total = 0
        #         sum = 0
        #         for result in record.school_student_ids:
        #             sum += result.max_marks
        #         record.total = sum
