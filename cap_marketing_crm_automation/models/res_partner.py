from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    marketing_language = fields.Selection([('en', 'English'), ('fr', 'French')], string='Marketing Language',
                                          store=True, compute='_compute_marketing_language')

    @api.depends('lang')
    def _compute_marketing_language(self):
        for rec in self:
            if not rec.lang:
                rec.marketing_language = ''
            elif rec.lang.startswith("fr"):
                rec.marketing_language = "fr"
            else:
                rec.marketing_language = "en"

