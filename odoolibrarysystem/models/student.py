from odoo import api, models, fields
# from datetime import datetime
from datetime import datetime, timedelta


class StudentClass(models.Model):
    _name = 'library.student'
    _description = 'library details '
    _order = 'id desc'

    name = fields.Char(string=" First Name: ", compute='_compute_names', store=True, compute_sudo=False)
    # name = fields.Char(string=" First Name: ")
    l_name = fields.Char(string=" last Name: ", compute='_compute_names', compute_sudo=False)
    full_name = fields.Char(string="full name")
    phone = fields.Char(string="Phone: ", copy=False)
    email = fields.Char(string="Email: ")
    gender = fields.Selection([('f_male', 'Female'), ('m_male', 'male'), ('transgender', 'Transgender')],
                              string="Gender: ")
    # student_dob = fields.Date(string="Date of Birth")
    # calc_age = fields.Integer(string="Age", compute="age_calc", store=True)

    address1 = fields.Char(string=" Street1 ")
    address2 = fields.Char(string=" Street2 ")
    state = fields.Char(string=" State ")
    pincode = fields.Char(string=" Pincode ")
    country = fields.Many2one('res.country', string="country")

    book_ids = fields.One2many(comodel_name='library.book', inverse_name='stu_rel_id', string="book")

    teacher_rel_id = fields.Many2one('library.teacher', string="teacher")

    prescription = fields.Html(string='enter prescription')

    #
    # @api.depends('full_name')
    # def _compute_f_name(self):
    #     for record in self:
    #         record.full_name = f"{record.name} + {record.l_name}"
    #         print("f>>>>>>>>>>>>>>>>>>>>", record.full_name)

    # @api.onchange('full_name')
    # def onchange_full_name(self):
    #     if self.full_name:
    #         names = self.full_name.split()
    #         self.name = names[0] if names else ''
    #         self.l_name = ' '.join(names[1:]) if len(names) > 1 else ''

    @api.depends('full_name')
    def _compute_names(self):
        for record in self:
            if record.full_name:
                names = record.full_name.split()
                record.name = names[0] if names else ''
                record.l_name = ' '.join(names[1:]) if len(names) > 1 else ''
            else:
                record.name = ''
                record.l_name = ''

    # def calculate_age(dob):
    #     today = datetime.today()
    #     birthdate = datetime.strptime(dob, '%Y-%m-%d')  # Assuming the date is in 'YYYY-MM-DD' format
    #     age1 = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    #     return age1
    #
    # # Example usage:
    # # birthday_date = '1990-05-15'
    # age1 = calculate_age(dob)
    # print(f"The person is {age1} years old.")

    # student_dob = fields.Date(string="Date of Birth")
    # calc_age = fields.Integer(string="Calculated Age", compute="age_calc", store=True)
    #

    # # Calculated age
    # @api.depends('dob')
    # def age_calc(self):
    #     # if self.dob is not False:
    #     if record in self:
    #         record.age = (datetime.today().date() - datetime.strptime(str(self.dob),
    #                                                                      '%Y-%m-%d').date()) // timedelta(days=365)

    student_dob = fields.Date(string="Date of Birth")
    calc_age = fields.Integer(string="Age", compute="age_calc", store=True, compute_sudo=False)

    # # Calculated age
    @api.depends('student_dob')
    def age_calc(self):
        for rec in self:
            if rec.student_dob is not False:
                rec.calc_age = (datetime.today().date() - datetime.strptime(str(self.student_dob),
                                                                            '%Y-%m-%d').date()) // timedelta(days=365)

    total = fields.Float(compute="_compute1_total", inverse="_inverse_total")
    amount = fields.Float()

    @api.depends("amount")
    def _compute1_total(self):
        for record in self:
            record.total = 2.0 * record.amount

    def _inverse_total(self):
        for record in self:
            record.amount = record.total / 2.0



    def check_orm(self):
        res = self.env['library.student'].search([])
        for record in res:
            print("name: ", record.name, "age", record.age)



