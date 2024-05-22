from odoo import models,fields,api,_


class LibraryBook(models.Model):
    _name = 'library.user'

    name = fields.Char('Name')

    book_id = fields.Many2one('library.book',string='Book Id')


    related_m2m = fields.Many2many(related='book_id.so_ids',string='related m2m so_ids',store=True)
