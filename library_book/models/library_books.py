from odoo import models,fields,api,_


class LibraryBook(models.Model):
    _name = 'library.book'


    name = fields.Char('Book Title')
    author = fields.Char('Author')
    date_of_publication = fields.Date('Publish Date')
    price = fields.Integer('Price')