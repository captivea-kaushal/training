from odoo import api, models, fields


class CrmleadExtend(models.Model):
    _inherit = 'crm.lead'

    # custom_lead_data1_id = fields.Many2many('sale.order')

    # def action_sale_quotations_new(self):
    #     if not self.partner_id:
    #         return self.env["ir.actions.actions"]._for_xml_id("sale_crm.crm_quotation_partner_action")
    #     else:
    #         return self.action_new_quotation()

    #
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

#     @api.model
#     def create(self, values):
#         # Create the sale order record
#         order = super(SaleOrder, self).create(values)
#
#         # Create a corresponding CRM lead record
#         crm_lead = self.env['crm.lead'].create({
#             'name': order.name,
#             'contact_name': order.partner_id.name,
#             'email_from': order.partner_id.email,
#             # Add any other fields you want to copy from the sale order
#         })
#
#         return order
#
#
# class SaleOrderTag(models.Model):
#     _name = 'sale.order.tag'
#     _description = 'Sale Order Tag'
#
#     name = fields.Char(string='Name', required=True)


# class Crmleadextend(models.Model):
#     _inherit = 'crm.lead'
#
#     crm_lead_same_data_id = fields.Many2one('crm.lead')
#
#     def _default_tag_ids(self):
#         tag_obj = self.env['crm.lead.tag']
#         tag = tag_obj.search([('name', '=', 'From Lead')], limit=1)
#         return [(4, tag.id)] if tag else []
#
#     tag_ids = fields.Many2many('crm.lead.tag', default=_default_tag_ids)


# @api.model
# def create(self, vals):
#     if 'opportunity_id' in vals:
#         lead = self.env['crm.lead'].browse(vals['opportunity_id'])
#         if lead:
#             # tag_from_lead = self.env.ref('crm.crm_lead_view_form')
#             tag_from_lead = self.env.ref('crm.crm_lead_view_form')
#             if tag_from_lead:
#                 # vals['tag_ids'] = [(4, tag_from_lead.id)]
#                 vals['tag_ids'] = [(4, tag_from_lead.id)]
#     return super(SaleOrderExtend, self).create(vals)

# @api.onchange('custom_lead_data1_id')
# def onchange_crm_id(self):
#     self.tag_ids = self.custom_lead_data_ids.tag_ids
