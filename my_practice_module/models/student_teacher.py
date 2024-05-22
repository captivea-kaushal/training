from odoo import fields, models, api
from datetime import datetime, timedelta
from odoo.osv import expression


class StudentTeacher(models.Model):
    _name = 'practice.student.teacher'
    _description = 'Details of Teacher'
    _rec_name = 'teacher_name'

    teacher_name = fields.Char(string='Teacher Name')

    subject = fields.Char(string='Subject')
    date_of_joining = fields.Date(string='Date of joining')

    # student_id = fields.Many2one('practice.student.profile',string='Student_id')
    #
    # related_of_m2m_ids = fields.Many2many(related='student_id.result_ids', string='related_of_m2m_ids', readonly=False)
    #
    # related_new_m2m_ids = fields.Many2many(related='student_id.crm_lead_ids', string='related_of_m2m_new_ids', readonly=False,store=True)

    is_active = fields.Boolean(string='Is Active')
