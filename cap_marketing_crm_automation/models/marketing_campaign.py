# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class MarketingCampaignInherit(models.Model):
    _inherit = 'marketing.campaign'

    def action_show_opportunity(self):
        return {'type': 'ir.actions.act_window',
                'name': 'Opportunity',
                'view_mode': 'kanban,tree,form',
                'res_model': 'crm.lead',
                'domain': [('campaign_id', '=', self.utm_campaign_id.id)]}
