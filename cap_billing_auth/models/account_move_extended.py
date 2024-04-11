from odoo import models,fields,api,_
from odoo.exceptions import AccessError

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):

        move = super(AccountMove, self).create(vals)

        # Check if partner_id exists in bill.auth
        authorization = self.env['bill.auth'].search([('partner_id', '=', move.partner_id.id)])
        if not authorization:
            return move  # Allow creation if partner not found in bill.auth

        else:
            for line in move.invoice_line_ids:
                if line.product_id and line.account_id:
                    authorization = self.env['bill.auth'].search([
                        ('partner_id', '=', move.partner_id.id),
                        ('allowed_product_ids', 'in', line.product_id.id),
                        ('allowed_account_ids', 'in', line.account_id.id)
                    ])
                    print('************',authorization)
                    if not authorization:
                        allowed_products_and_accounts = self.env['bill.auth'].search([('partner_id', '=', move.partner_id.id)])

                        if allowed_products_and_accounts:
                            allowed_products = ', '.join(allowed_products_and_accounts.mapped('allowed_product_ids.name'))
                            allowed_accounts = ', '.join(allowed_products_and_accounts.mapped('allowed_account_ids.name'))
                            raise AccessError(_("The selected vendor only have authorization for the following products and accounts. \n\nAllowed products: %s\nAllowed accounts: %s") % (allowed_products, allowed_accounts))
                        else:
                            raise AccessError(_("The selected vendor dose not have authorization for any products or accounts !!\n\nPlease Contact Administration for Authorization"))

        return move