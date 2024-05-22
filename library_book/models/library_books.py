from odoo import models,fields,api,_

class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char('Book Title')
    author = fields.Char('Author')
    date_of_publication = fields.Date('Publish Date')
    price = fields.Integer('Price')

    so_ids = fields.Many2many('crm.lead',string='CRM IDS')

    # @api.model
    # def create(self,vals):
    #     print('vals in model', vals)
    #     res = super(LibraryBook,self).create(vals)
    #
    #     user = self.env['library.user'].create([{'name':vals['name']},{'name':'first'},{'name':'second'},{'name':'third'},{'name':'fourth'}])
    #
    #     print('res in model',res)
    #
    #     return res

    # @api.model_create_multi
    # def create(self, vals):
    #     created_users = []
    #
    #     print('vals in create multi',vals)
    #
    #     # Iterate over each dictionary in vals (each represents a record to create)
    #     for val in vals:
    #         # Create a library user with the name from the current dictionary
    #         user = self.env['library.user'].create({'name': val['name']})
    #         # Append the created user to the list
    #         created_users.append(user)
    #
    #     # You can use the created_users list for further processing if needed
    #
    #     # Call the super method to create library books
    #     res = super(LibraryBook, self).create(vals)
    #     print('res in create multi model',res)
    #
    #     return res
