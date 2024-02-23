from odoo import models,api,fields

class SaleOrderExtended(models.Model):
    _inherit = 'sale.order'

    test_crm_lead_id = fields.Many2one('crm.lead',string='Extended Crm Lead Field')

    new_tag_ids = fields.Many2many('crm.tag',string='New Tag Field')

    # @api.model
    # def create(self, values):
    #
    #     order = super(SaleOrderExtended, self).create(values)
    #     if order.opportunity_id:
    #         order.tag_ids = order.opportunity_id.tag_ids
    #
    #     return order

