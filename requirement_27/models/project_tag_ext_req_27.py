from odoo import fields, models, api


class ProjectTags(models.Model):
    _inherit = 'project.tags'

    users_who_worked_ids = fields.Many2many('res.users', compute='_compute_users_who_worked', store=False,string='Users Who Worked')

    @api.depends('task_ids.user_ids', 'task_ids')
    def _compute_users_who_worked(self):
        for record in self:
            users_set = set()
            for task in record.task_ids:
                print('task :', task)
                users_set = users_set.union(set(task.user_ids.ids))
                print('user_set', users_set)
            record.users_who_worked_ids = [(6, 0, list(users_set))]
