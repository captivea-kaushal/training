from odoo import api, models, fields


class CrmleadExtend(models.Model):
    _inherit = 'crm.lead'

   
    def _prepare_opportunity_quotation_context(self):
        print('in custom model', self)
        required_tag = self.env['crm.tag'].search([('name', '=', 'from lead')])
        print('required_tag', required_tag)
        self.ensure_one()
        quotation_context = {
            'default_opportunity_id': self.id,
            'default_partner_id': self.partner_id.id,
            'default_campaign_id': self.campaign_id.id,
            'default_medium_id': self.medium_id.id,
            'default_origin': self.name,
            'default_source_id': self.source_id.id,
            'default_company_id': self.company_id.id or self.env.company.id,
            'default_tag_ids': [(6, 0, self.tag_ids.ids), (4, required_tag.id)]
        }
        print('before', quotation_context)
        # quotation_context = {'default_tag_ids': [(4,required_tag.id)]}
        print('after', quotation_context)
        if self.team_id:
            quotation_context['default_team_id'] = self.team_id.id
        if self.user_id:
            quotation_context['default_user_id'] = self.user_id.id
        return quotation_context

