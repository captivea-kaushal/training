from odoo import api, models, fields


class Requirement_question(models.Model):
    # _name = 'requirement.question'
    _inherit = 'sale.order'
    # _description = "requirement question"

    n = fields.Char(string="name")
    customer_street = fields.Char(related='partner_id.street', string='Customer Street')
    customer_street2 = fields.Char(related='partner_id.street2', string='Customer Street 2')
    customer_country_id = fields.Many2one(related='partner_id.country_id', string='Customer Country')
    customer_state_id = fields.Many2one(related='partner_id.state_id', string='Customer State')
    customer_city = fields.Char(related='partner_id.city', string='Customer City')
    customer_zip = fields.Char(related='partner_id.zip', string='Customer Zip')

