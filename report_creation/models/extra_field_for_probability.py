from odoo import models, fields,api

class CustomCrmLeadScoringFrequencyField(models.Model):
    _inherit = 'crm.lead'

    # Add your additional fields here
    technology = fields.Selection(
        [
            ('python', 'Python'),
            ('java', 'Java'),
            ('c++', 'C++'),
            ('js', 'Js'),
        ],
        string='Technology',
    )