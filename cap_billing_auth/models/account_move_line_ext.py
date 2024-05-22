from odoo import models, fields, api, _
from odoo.exceptions import AccessError, ValidationError


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.model
    def create(self,vals):
        move = super(AccountMoveLine, self).create(vals)

        authorization = self.env['bill.auth'].search([('partner_id', '=', move.move_id.partner_id.id)])

        if authorization:
            for line in move.move_id.invoice_line_ids:
                allowed_products = authorization.allowed_product_ids.ids
                # print('allowed_products in line create', allowed_products)
                # print('product id in vals in create', line.product_id.id)
                allowed_accounts = authorization.allowed_account_ids.ids
                # print('allowed account in line create', allowed_accounts)
                # print('account id in vals in create', line.account_id.id)

                if line.product_id.id not in allowed_products:
                    raise ValidationError(_('Selected product is not allowed for this partner.'))
                elif line.account_id.id not in allowed_accounts:
                    raise ValidationError(_('Selected account is not allowed for this partner.'))
        return move

    def write(self, vals):
        res = super(AccountMoveLine, self).write(vals)
        for line in self.move_id.invoice_line_ids:

            if 'account_id' in vals or 'product_id' in vals:
                authorization = self.env['bill.auth'].search([('partner_id', '=', self.move_id.partner_id.id)])
                if authorization:
                    allowed_accounts = authorization.allowed_account_ids.ids
                    allowed_products = authorization.allowed_product_ids.ids
                    print('ac id in vals', line.account_id.id)
                    if line.account_id.id not in allowed_accounts:
                        raise ValidationError(_('You are not allowed to change to this account.'))
                    if line.product_id.id not in allowed_products:
                        raise ValidationError(_('You are not allowed to change to this product.'))
            # elif 'product_id' in vals:
            #     authorization = self.env['bill.auth'].search([('partner_id', '=', self.move_id.partner_id.id)])
            #     if authorization:
            #         allowed_products = authorization.allowed_product_ids.ids
            #         if line.product_id.id not in allowed_products:
            #             raise ValidationError(_('You are not allowed to change to this product.'))

        return res


    #     if vals.get('product_id'):
    #         bill_auth = self.env['bill.auth'].search([('partner_id', '=', self.move_id.partner_id.id)])
    #         if bill_auth:
    #             allowed_products = bill_auth.allowed_product_ids.ids
    #             print('allowed products in write', allowed_products)
    #             print('product id in vals in write', vals.get('product_id'))
    #
    #             if vals.get('product_id') not in allowed_products:
    #                 raise ValidationError(_('Selected product is not allowed for this partner.'))
    #
    #     if vals.get('account_id'):
    #         bill_auth = self.env['bill.auth'].search([('partner_id', '=', self.move_id.partner_id.id)])
    #         if bill_auth:
    #             allowed_accounts = bill_auth.allowed_account_ids.ids
    #             print('allowed account in write', allowed_accounts)
    #             print('account id in vals in write', vals.get('account_id'))
    #             if vals.get('account_id') not in allowed_accounts:
    #                 raise ValidationError(_('Selected account is not allowed for this partner.'))
