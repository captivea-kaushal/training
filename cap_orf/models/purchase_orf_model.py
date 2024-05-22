from odoo import fields,models,api,_

class PurchaseOrf(models.Model):
    _name = 'purchase.orf'
    _description = 'Order Request Form'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name',default='NEW',readonly=True)
    vendor_name_id = fields.Many2one('res.partner',string='Vendor',required=True)
    vendor_reference = fields.Char('Vendor Reference')
    currency_id = fields.Many2one('res.currency',string='Currency',required=True,default=lambda self: self.env.company.currency_id)
    po_date = fields.Date('PO DATE')
    destination_detail = fields.Selection([('ddc', 'DDC'),('poe', 'POE'),('fob', 'FOB')],required=True,string='Destination Detail')
    order_line_ids = fields.One2many('order.line','purchase_orf_id',string='Product',readonly=True, states={'draft': [('readonly', False)], 'orf_in_progress': [('readonly', False)]})
    state = fields.Selection([('draft', 'Draft'),('orf_in_progress', 'In Progress'),('confirm', 'Confirm')],default='draft')

    total_tax = fields.Float(compute="_compute_total_tax",string='Total',readonly=True)

    @api.depends('order_line_ids.subtotal')
    def _compute_total_tax(self):
        for record in self:
            x = 0.0
            for line in record.order_line_ids:
                x += line.subtotal
            record.total_tax = x


    @api.model
    def create(self, vals):
        if vals.get('name', 'NEW') == 'NEW':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.orf.sequence')
        return super(PurchaseOrf, self).create(vals)

    def action_orf_in_progress(self):
        self.state = 'orf_in_progress'
        self.message_post(body=_("ORF in progress"), subtype_id=self.env.ref('mail.mt_note').id)

    def action_confirm_purchase(self):
        self.state = 'confirm'
        self.message_post(body=_("ORF Confirmed"), subtype_id=self.env.ref('mail.mt_note').id)

        request_for_quotation_vals = {'name': self.name,
                                      'partner_id':self.vendor_name_id.id,
                                      'date_approve':self.po_date,
                                      'partner_ref':self.vendor_reference,
                                      'currency_id':self.currency_id.id,
                                      'destination_detail':self.destination_detail,
                                      'purchase_orf_id':self.id,}

        create_rfq = self.env['purchase.order'].create(request_for_quotation_vals)

        for line in self.order_line_ids:
            purchase_order_line_vals = {'order_id':create_rfq.id,
                                        'product_id':line.product_id.id,
                                        'product_qty':line.quantity,
                                        'product_uom':line.uom_id.id,
                                        'price_unit':line.unit_price,}

            self.env['purchase.order.line'].create(purchase_order_line_vals)