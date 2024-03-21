from odoo import api, models, fields


class SubjectClass(models.Model):
    _name = 'library.subject'
    _description = 'book subject details '
    _rec_name = ('subject')

    subject = fields.Char(string='subject name')
