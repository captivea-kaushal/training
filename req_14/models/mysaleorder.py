from odoo import api, models, fields

#
# class mysubject(models.Model):
#     _name = 'my.subject'
#     _description = "my sale data"
#
#     subject_name = fields.Char(string="sunject name")
#     book_lang = fields.Char(string="book language ")


class mysaledata(models.Model):
    _name = 'my.saledata'
    _description = "my sale data"
    _inherit = 'hospital.patient'

    hos_owner_name = fields.Char(string="Hospital owner name")


















# sale_order_extended .access_my_subject,access_my_subject,sale_order_extended .model_my_subject,base.group_user,1,1,1,1
