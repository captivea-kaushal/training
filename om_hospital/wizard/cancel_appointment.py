from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'
    _rec_name = 'appointment_id'

    appointment_id = fields.Many2one('hospital.appointment', string="appointment id")
    # ,domain = [('state','=','draft')]
    # , domain=[('state', 'in', ['draft', 'In_progress'])])
    # , domain=[('priority', 'in', ['0', '1'])])

    today_cancel = fields.Date(default=fields.Date.today())
    text_reason = fields.Text(string="Reason Text")

    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_('sorry you cant use the same day of cancellation!'))
        return
    #
    # _sql_constraints = [
    #     ('appointment_id_uniq', 'unique (appointment_id)', 'every person tag must be unique !')
    # ]

