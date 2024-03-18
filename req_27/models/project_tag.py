from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'


class ProjectTags(models.Model):
    _inherit = 'project.tags'

    task_ids = fields.Many2many('project.task', string='Tasks')
    users_worked = fields.Many2many('res.users', string='Users', compute='_compute_users', store=False)

    @api.depends('task_ids.user_ids')
    def _compute_users(self):
        for tag in self:
            users = tag.task_ids.mapped('user_ids')
            tag.users_worked = [(6, 0, users.ids)]
