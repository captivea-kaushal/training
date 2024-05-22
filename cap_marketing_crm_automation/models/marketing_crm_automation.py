# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.fields import Datetime
import logging

_logger = logging.getLogger(__name__)


class MarketingCrmAutomation(models.Model):
    _inherit = 'marketing.activity'

    activity_type = fields.Selection(selection_add=[('opportunity', 'Opportunity')],
                                     ondelete={'opportunity': 'cascade'})
    company_id = fields.Many2one('res.company', string='Company')
    medium_id = fields.Many2one('utm.medium', 'Medium',
                                help="This is the method of delivery, "
                                     "e.g. Postcard, Email, or Banner Ad")
    source_id = fields.Many2one('utm.source', 'Source',
                                help="This is the source of the link, "
                                     "e.g. Search Engine, another domain, or name of email list")
    team_id = fields.Many2one('crm.team', string='Sales Team')
    description = fields.Html('Description')

    def _execute_opportunity(self, traces):
        traces_ok = self.env['marketing.trace']
        opportunity = []
        stage_id = self.env['crm.stage'].search([], limit=1, order='sequence asc')
        for trace in traces:
            opportunity_vals = {
                'stage_id': stage_id.id,
                'name': self.name,
                'partner_name': trace.participant_id.resource_ref.name,
                'medium_id': self.medium_id.id,
                'source_id': self.source_id.id,
                'team_id': self.team_id.id,
                'description': self.description,
                'campaign_id': self.campaign_id.utm_campaign_id.id,
                'street': trace.participant_id.resource_ref.street,
                'street2': trace.participant_id.resource_ref.street2,
                'city': trace.participant_id.resource_ref.city,
                'state_id': trace.participant_id.resource_ref.state_id.id,
                'zip': trace.participant_id.resource_ref.zip,
                'country_id': trace.participant_id.resource_ref.country_id.id,
                'website': trace.participant_id.resource_ref.website,
                'function': trace.participant_id.resource_ref.function,
                'mobile': trace.participant_id.resource_ref.mobile,
                'contact_name': trace.participant_id.resource_ref.name,
                'title': trace.participant_id.resource_ref.title.id,
                'phone': trace.participant_id.resource_ref.phone,
                'email_from': trace.participant_id.resource_ref.email,
                'user_id': False,
            }
            opportunity.append(opportunity_vals)
        try:
            self.env['crm.lead'].create(opportunity)
        except Exception as e:
            _logger.warning(
                'Marketing Automation: activity <%s> encountered Opportunity creation issue %s',
                self.id, str(e), exc_info=True)
            trace.write({
                'state': 'error',
                'schedule_date': Datetime.now(),
                'state_msg': _('Exception in Opportunity Creation: %s', e),
            })
        else:
            traces_ok |= traces

        # Update status
        traces_ok.write({
            'state': 'processed',
            'schedule_date': Datetime.now(),
        })
        return True
