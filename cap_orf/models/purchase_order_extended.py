from odoo import fields,models,api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    date_approve = fields.Datetime('PO DATE', readonly=1, index=True, copy=False)

    destination_detail = fields.Selection([('ddc', 'DDC'), ('poe', 'POE'), ('fob', 'FOB')],string='Destination Detail',readonly=True)
    purchase_orf_id = fields.Many2one('purchase.orf',string='Purchase ORF',readonly=True)