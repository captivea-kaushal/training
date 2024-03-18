from odoo import api, models, fields


class RequirementSale(models.Model):
    _name = 'req.rep'
    _description = "req rep task"

    country_id = fields.Many2one('res.country', string="country name")
    country_code_id = fields.Char(string="country code", related="country_id.code")
