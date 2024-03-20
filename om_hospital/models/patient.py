from odoo import api, models, fields, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError


class TeacherClass(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
        # 'utm.mixin',
        'format.address.mixin',
    ]
    # _inherit = 'sale.order'
    # state = fields.Selection([
    #     ('draft', 'draft'), ('in_consultation', 'In consultation'),
    #     ('done', 'Done'), ('cancel', 'cancelled')
    # ], default='draft', string="status")
    # _rec_name = 'selected_subject'
    new_num = fields.Char(string="NEW")
    name = fields.Char(string="Name", tracking=True, copy=False)
    student_dob = fields.Date(string="date of birth")
    calc_age = fields.Integer(string="Age", compute='compute_calc_age', store=True)
    # calc_age = fields.Integer(string="Age")
    ref = fields.Char(string="Reference ")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'other')])
    is_true = fields.Boolean(string="Archived")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tag records")

    parent = fields.Char(string="Parent")
    marital_status = fields.Selection([('married', 'Married'), ('single', 'Single')], string="Marital status")
    partner_name = fields.Char(string="Partner name")

    company_name = fields.Char(string="company name")
    CO_REGN_NO = fields.Char(string="CO_REGN_NO")
    Venture_Drive = fields.Date(string="2_Venture_Drive")
    Vision_Exchange = fields.Char(string="Vision_Exchange")
    Tel = fields.Char(string="Telephone number")
    Fax = fields.Char(string="Fax:")
    Email = fields.Char(string="Email")
    website_url = fields.Char(string="website_url")
    booking_date = fields.Date(string="Booking date", default=fields.Date.context_today)

    # @api.depends('appointment_ids')
    # def _compute_appointment_count(self):
    #     for rec in self:
    #         rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    # SHIPPER = fields.Char(string="SHIPPER:")
    # VENTURE_DRIVE_1 = fields.Date(string="2_Venture_Drive")
    # VISION_EXCHANGE_1 = fields.Char(string="Vision_Exchange")
    # Tel1 = fields.Char(string="Telephone number")
    # FAX1 = fields.Char(string="FAX:")
    # EMAIL = fields.Char(string="EMAIL:")
    #
    # address = fields.Char(string="ADDRESS")
    # pincode = fields.Char(string="PINCODE")
    # country = fields.Many2one('res.country', string="Country Name")
    # state = fields.Many2one('res.country.state', string="State Name")
    # Gstin_no = fields.Char(string="GSTIN NO")
    # iec_no = fields.Char(string="IEC NO")
    # pan_no = fields.Char(string="PAN NO")
    # email = fields.Char(string="EMAIL")
    #
    # bl_no = fields.Char(string="BL NO")
    # bl_date = fields.Char(string="BL DATE")
    # invoice_no = fields.Char(string="INVOICE NO")
    # invoice_date = fields.Char(string="INVOICE DATE")
    # batch_no = fields.Char(string="BATCH NO")
    # manufacturing_date = fields.Char(string="MANUFACTURING DATE")
    # expiry_date = fields.Char(string="EXPIRY DATE")
    # total_net_weight = fields.Char(string="TOTAL NET WEIGHT")
    #
    # container_and_seal_number = fields.Char(string="CONTAINER AND SEAL NUMBER")

    @api.constrains('student_dob', 'calc_age')
    def _check_student_dob(self):
        print("self rec", self)
        for record in self:
            if record.calc_age < 1:
                raise ValidationError("The age  cannot be o any person")
            if record.student_dob > fields.Date.today():
                raise ValidationError("The end date cannot be set in the past")

    @api.model
    def create(self, vals):
        print("create method is triggered")
        res = super(TeacherClass, self).create(vals)

        print(">>>>>>>>>>> self", self)
        print(">>>>>>>>>>> vals", vals)
        print(">>>>>>>>>>> res.name", res)
        return res

    def write(self, vals):
        print("write method executed", self, self.name)
        prev_name = self.name
        res = super(TeacherClass, self).write(vals)
        print("res....", res)
        print("vals.....", vals)
        if vals and vals.get('name'):
            if prev_name != vals.get('name'):
                raise ValidationError('Cant change the name')
        return res

    @api.model
    def default_get(self, vals):
        print("default get executed...")
        res = super(TeacherClass, self).default_get(vals)
        print("res default values", res)
        print("self default values", self)
        print("vals default values", vals)
        return res

    # @api.model
    def name_get(self):
        result = []
        print("record in self", self)
        for record in self:
            # res = '[' + record.name + ']' + ' ' + record.ref
            # result.append((record.id, res))
            # print("name get record", result)
            result.append((record.id, '%s %s' % (record.name, record.ref)))
        print("result.....", result)
        return result

    def mysearch_button(self):
        print("search method response.......")
        res = self.env['hospital.patient'].search(['gender', '==', 'male'], )
        print("res.............>>>>>>>>>", res)
        for record in res:
            print("record......", record.name, record.calc_age)

    # # Calculated age
    @api.depends('student_dob')
    def compute_calc_age(self):
        for rec in self:
            if rec.student_dob is not False:
                rec.calc_age = (datetime.today().date() - datetime.strptime(str(self.student_dob),
                                                                            '%Y-%m-%d').date()) // timedelta(days=365)

    @api.model
    def create(self, vals):
        if vals.get('reference_no', _('New')) == _('New'):
            vals['new_num'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        return super(TeacherClass, self).create(vals)

    def check_read_group(self):
        grouped_result = self.read_group(
            [('is_true', "!=", False)],  # domain
        )
        print("read group reurn result...", grouped_result)
        return grouped_result

    # @api.ondelete(at_uninstall=False)
    # def _unlink_if_no_variant(self):
    #     if self.variant_report_ids:
    #         raise ValidationError(("You can't delete a report that has variants."))
