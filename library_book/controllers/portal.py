from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request

class NewPortalClass(CustomerPortal):

    def _prepare_home_portal_values(self,counters):
        rtn = super(NewPortalClass,self)._prepare_home_portal_values(counters)

        rtn['library_book_counts']=request.env['library.book'].search_count([])
        return rtn