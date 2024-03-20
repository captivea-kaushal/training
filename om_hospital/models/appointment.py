from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = "hospital appointment"
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
        # 'utm.mixin',
        'format.address.mixin',
    ]
    _rec_name = "patient_id"
    # , ondelete = 'cascade'
    patient_id = fields.Many2one('hospital.patient', string="patients", ondelete='restrict')
    # you  can change the value for selection fields because you give readonly parameter
    # gender = fields.Selection(
    #     string="Gender", related='patient_id.gender',readonly = False)
    gender = fields.Selection(
        string="Gender", related='patient_id.gender')
    ref = fields.Char(string="Reference ")
    appointment_time = fields.Datetime(string="Appointment time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking date", default=fields.Date.context_today,
                               help="this is booking date fields")
    prescription = fields.Html(string="prescription")
    docter_id = fields.Many2one('res.users', string="Docter")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority", index=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('In_progress', 'In progress'),
        ('done', 'Done'),
        ('cancel', 'cancelled')], default="draft", string='status')
    new_num_appoint = fields.Char()

    pharmacy_line_ids = fields.One2many("appointment.pharmacy.lines", "appointment_id", string="pharmacy line")
    hide_sales_price = fields.Boolean(string="Hide sales price ")

    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count")

    def In_progress_action(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'In_progress'

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def click_button(self):
        print("button clicked......")

    def action_In_progress(self):
        for record in self:
            record.state = 'In_progress'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_rainbow(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "completed successfully",
                'type': 'rainbow_man',
            }
        }

    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.model
    def create(self, vals):
        if vals.get('reference_no', _('New')) == _('New'):
            vals['new_num_appoint'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        return super(HospitalAppointment, self).create(vals)

    def unlink(self):
        for rec in self:
            if rec.state == 'done':
                raise ValidationError("you can't delete this record because this is done state !!")
            return super(HospitalAppointment, self).unlink()


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one("product.product", string="product")
    price_unit = fields.Float(string="price ", related='product_id.list_price')
    qty = fields.Integer(string="quantity", default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="appointment name")
