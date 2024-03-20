from odoo import api, models, fields
from datetime import date, datetime, timedelta


class AccountClass(models.Model):
    _inherit = 'account.move'