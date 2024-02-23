from odoo import fields,api,models

class ReportDetails(models.Model):
    _name = 'report_creation.report_details'
    _description = 'generates reports as per requirements'

    shipper_company_logo = fields.Image(string='Shipper Logo', help='Select an image file')
    company_logo_details = fields.Text(string='Company details')
    certificate_date = fields.Date(string='Today\'s Date', default=fields.Date.today)
    shipper = fields.Text(string='SHIPPER')
    consignee = fields.Text(string='CONSIGNEE & NITIFY PARTY')
    bl_no = fields.Char(string='BL NO')
    bl_date = fields.Date(string='BL DATE')
    invoice_no = fields.Char(string='INVOICE NO')
    invoice_date = fields.Date(string='INVOICE DATE')
    batch_no = fields.Char(string='BATCH NO')
    manufacturing_date = fields.Date(string='MANUFACTURING DATE')
    expiry_date = fields.Date(string='EXPIRY DATE')
    total_net_weight = fields.Char(string='TOTAL NET WEIGHT')
    container_no = fields.Char(string='CONTAINER NO')
    seal_no = fields.Char(string='SEAL NO')
    authorise_signatory = fields.Image(string='Shipper Logo', help='Select an image file')

