from odoo import api, models, fields


class StudentClass(models.Model):
    _name = 'student.school'
    _description = 'school details system'

    name = fields.Char(string=" First Name: ")
    l_name = fields.Char(string=" last Name: ")
    age = fields.Integer(string="Age: ")
    phone = fields.Char(string="Phone: ")
    email = fields.Char(string="Email: ")
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection([('f_male', 'Female'), ('m_male', 'male'), ('transgender', 'Transgender')],
                              string="Gender: ")
    highest_qualification = fields.Char(string="Highest Qualification: ")
    _order = 'id desc'

    # address
    address1 = fields.Char(string="Address1")
    address2 = fields.Char(string="Address2")
    pincode = fields.Char(string="Pincode")
    country = fields.Many2one('res.country')
    state = fields.Many2one('res.country.state')
    # currency = fields.Many2one('res.currency')

    # father information
    father_name = fields.Char(string="Father name")
    f_occupation = fields.Char(string="Father Occupation")
    f_age = fields.Char(string="Father age")
    f_phone = fields.Char(string="Father phone")
    moth_name = fields.Char(string="mother name")
    m_occupation = fields.Char(string="mother Occupation")
    m_age = fields.Char(string="mother age")
    parent_annual_income = fields.Char(string="Parents Annual Income")

    f_address1 = fields.Char(string="Address1")
    f_address2 = fields.Char(string="Address2")
    f_pincode = fields.Char(string="Pincode")
    country1 = fields.Many2one('res.country')
    state1 = fields.Many2one('res.country.state')

    total = fields.Float(string="Total", compute="_compute_school_obtain_marks_percent")
    obtain_marks_percent = fields.Float(string="obtain_marks_total", compute="_compute_school_obtain_marks_percent")

    school_student_ids = fields.One2many(comodel_name='result.student', inverse_name='result_id')

    total_percent = fields.Float(string="Total percent result: ", compute="_compute_school_obtain_marks_percent")

    qualification_ids = fields.One2many('student.qualification', 'qualification_relation_id')




    # subject_id = fields.Many2one('student.subject')
    # @api.depends('school_student_ids')
    # def _compute_school_student(self):
    #     for record in self:
    #         record.total = 0
    #         sum = 0
    #         for result in record.school_student_ids:
    #             sum += result.max_marks
    #         record.total = sum

    @api.depends('school_student_ids', 'obtain_marks_percent', 'total')
    def _compute_school_obtain_marks_percent(self):
        for record in self:
            sum_obtain_marks_percent = 0
            record.total = 0
            record.total_percent = 0
            sum = 0
            for result in record.school_student_ids:
                sum += result.max_marks
                sum_obtain_marks_percent += result.marks_obtained

                # all_percent += sum_obtain_marks_percent * sum / 100
            record.total = sum
            print('total>>>', record.total)
            record.obtain_marks_percent = sum_obtain_marks_percent
            print('obtained marks>>>>>>.', record.obtain_marks_percent)
            if record.obtain_marks_percent == False:
                break
            else:
                record.total_percent = float(100 * sum_obtain_marks_percent) / sum

            print('total_percent>>>>>>.', record.total_percent)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name must be unique !'),
        ('age_uniq', 'CHECK(age >= 18)', 'The age number of must be greater than 18 years old.')
    ]
    # _sql_constraints = [
    #     ('qualification_uniq', 'unique (qualification_ids)', 'The phone qualification  must be unique !')
    # ]

    _sql_constraints = [
        ('qualification_uniq', 'unique (qualification_ids.name)', 'The phone qualification  must be unique !')
    ]

    # @api.constrains('qualification_ids')
    # def _check_child_values(self):
    #     for record in self:
    #         # Example constraint: Ensure that the sum of values in child records is less than 100.
    #         if sum(record.child_ids.mapped('value')) > 100:
    #             raise models.ValidationError("Sum of child values cannot exceed 100.")
