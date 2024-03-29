from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class PurchaseORFPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        res = super(PurchaseORFPortal, self)._prepare_home_portal_values(counters)

        res['purchase_orf_count'] = request.env['purchase.orf'].search_count([])
        return res

    @http.route(['/purchase_orf'], type='http', website=True)
    def purchase_orf_portal_list_view(self, sortby=None, **kwargs):
        searchbar_sorting = {
            'id': {'label': _('ID'), 'order': 'id asc'},
            'name': {'label': _('Name'), 'order': 'name'},
        }
        if not sortby:
            sortby = 'id'

        orf = request.env['purchase.orf']
        order = searchbar_sorting[sortby]['order']
        orf_purchase = orf.search([], order=order)
        return request.render("cap_orf.purchase_orf_tree_portal_template", {
            'orf_purchase': orf_purchase,
            'page_name': 'purchase_orf_tree_page',
            'searchbar_sorting': searchbar_sorting,
            'sortby': sortby
        })

    @http.route(['/purchase_orf/<int:orf_id>'], type='http', website=True)
    def purchase_orf_portal_form_view(self, orf_id, **kw):
        orf = request.env['purchase.orf'].browse(orf_id)
        vals = {"orf": orf, 'page_name': 'purchase_orf_form_page'}

        return request.render("cap_orf.purchase_orf_form_portal_template", vals)

