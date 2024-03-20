from odoo import models, api, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm_and_validate_delivery(self):
        # self.action_confirm()
        super(SaleOrder, self).action_confirm()

        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                "It is not allowed to confirm an order in the following states: %s",
                ", ".join(self._get_forbidden_state_confirm()),
            ))
        self.order_line._validate_analytic_distribution()
        for order in self:
            order.validate_taxes_on_sales_order()
            if order.partner_id in order.message_partner_ids:
                continue
            order.message_subscribe([order.partner_id.id])

        self.write(self._prepare_confirmation_values())


        context = self._context.copy()
        context.pop('default_name', None)

        self.with_context(context)._action_confirm()

        if self[:1].create_uid.has_group('sale.group_auto_done_setting'):
            self.action_done()

        return True

# Model
#
# sale.order
#
# Add a button of type object in sale.order
#
# When that button is clicked, try to perform following operations
#
# Confirm the order
#
# Validate the delivery order
# #
