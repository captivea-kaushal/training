from odoo import fields, models,api


class CrmLeadExtended(models.Model):
    _inherit = "crm.lead"

    @api.model
    def _prepare_opportunity_quotation_context(self):

        context = super(CrmLeadExtended, self)._prepare_opportunity_quotation_context()

        all_tag_ids_from_crm_lead = self.tag_ids.ids

        specific_tag_name = 'From Lead'
        specific_tag = self.env['crm.tag'].search([('name', '=', specific_tag_name)], limit=1)

        if specific_tag.id not in all_tag_ids_from_crm_lead:
            all_tag_ids_from_crm_lead.append(specific_tag.id)

        context['default_tag_ids'] = [(6, 0, all_tag_ids_from_crm_lead)]

        return context