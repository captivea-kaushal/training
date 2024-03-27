from odoo import http
from odoo.http import request


class LibraryController(http.Controller):

    @http.route('/library_book', auth='user', type='http', website=True)
    def library_book_list(self,**kw):
        user = request.env.user
        books = request.env['library.book']

        if user.has_group('library_book.group_library_admin'):
            books = books.search([])
        else:
            books = books.search([('create_uid', '=', user.id)])

        vals = {'books': books ,'page_name':'library_book_tree_view'}

        return request.render('library_book.library_book_tree_portal', vals)

    @http.route('/library_book/<int:book_id>', auth='user', type='http', website=True)
    def library_book_details(self, book_id, **kw):
        book = request.env['library.book'].browse(book_id)

        vals =  {'book': book, 'page_name':'library_book_form_view'}
        return request.render('library_book.library_book_form_portal',vals)