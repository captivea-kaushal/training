from odoo import api, models, fields, _


class Patient_Tag(models.Model):
    _name = 'patient.tag'
    _description = "Patient Tag"

    name = fields.Char(string="Name", required=True)
    is_true = fields.Boolean(string="active")
    color = fields.Integer(string="Color")
    sequence = fields.Integer(string="Sequence")

    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', 'every person tag name must be unique !'),
    # ]
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name of the language must be unique !'),
        ('sequence_uniq', 'check(sequence >= 0 and sequence <= 100)',
         'The expected number of sequence greater than must be positive.')
    ]

    # _sql_constraints = [
    #     ('sequence_uniq', 'CHECK(sequence >= 0)',
    #      'The expected number of sequence greater than must be positive.')
    #
    # ]
    # @api.returns('self')
    # def copy(self):
    #     for rec in self:
    #         if rec.is_true == False:
    #             rtn  = super(Patient_Tag, self).copy()
    #         return rtn

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('sequence', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super().fields_get(allfields, attributes)
        print("self record fields get after res...", self)
        print("rec fields get..", res)
        return res
