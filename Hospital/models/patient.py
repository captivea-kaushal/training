# from odoo import models, fields ,api
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient_records.customer'
    # _inherit = 'sale.order'
    _rec_nmae = 'dob'

    name = fields.Char(string="Name")
    dob = fields.Date(string="DOB", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'other')], string='Selection')
    is_child = fields.Boolean(string="enter value")
    # active = fields.Boolean(string="Active", default=True)
    notes = fields.Text(string='Terms and Conditions')
    # staff = fields.Selection([('male', 'male'), ('female', 'female')], string=" Hospital staff")


class hospital_inherit(models.Model):
    _inherit = 'sale.order'

    #
    #     # _inherit = 'sale.order'
    #
    staff = fields.Selection([('male', 'male'), ('female', 'female')], string=" Hospital staff")


class subham_ka_hospital(models.Model):
    _name = 'hospital.subham'
    _inherit = 'hospital.patient'

    subham_hos = fields.Selection([('male', 'male'), ('female', 'female')], string=" Hospital staff")
