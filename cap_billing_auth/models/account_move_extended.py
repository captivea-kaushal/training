from odoo import models, fields, api, _
from odoo.exceptions import AccessError, ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'


    # def write(self,vals):
    #     res = super(AccountMove, self).write(vals)
    #     print('vals*****',vals)
    #     # for line in self.invoice_line_ids:
    #     #     print('vals.....', vals.get('invoice_line_ids'))
    #     return res

    # @api.model
    # def create(self, vals):
    #     move = super(AccountMove, self).create(vals)
    #
    #     authorization = self.env['bill.auth'].search([('partner_id', '=', move.partner_id.id)])
    #
    #     if authorization:
    #         for line in move.invoice_line_ids:
    #             allowed_products = authorization.allowed_product_ids.ids
    #             print('allowed products in create', allowed_products)
    #             print('product id in vals in create', line.product_id.id)
    #             allowed_accounts = authorization.allowed_account_ids.ids
    #             print('allowed account in create', allowed_accounts)
    #             print('account id in vals in create', line.account_id.id)
    #
    #             if line.product_id.id not in allowed_products:
    #                 raise ValidationError(_('Selected product is not allowed for this partner.'))
    #             elif line.account_id.id not in allowed_accounts:
    #                 raise ValidationError(_('Selected account is not allowed for this partner.'))
    #     return move