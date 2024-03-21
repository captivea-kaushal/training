from odoo import api, models, fields
from datetime import date, datetime, time


class BookClass(models.Model):
    _name = 'library.book'
    _description = 'book details '

    book_no = fields.Char(string=" book number: ")
    isbn = fields.Char(string=" Isbn Number: ", size=5)
    book_title = fields.Char(string="Book Title: ")
    year_publish = fields.Date(string="Year Publish: ")
    date_arrived = fields.Date(string='Date Arrived', default=datetime.today())
    book_price = fields.Integer(string="Book Price: ")
    quantity = fields.Integer(string="quantity of book")
    auther_id = fields.Many2one('library.auther', string="auther")

    stu_rel_id = fields.Many2one('library.student', string="enter student name")

    subject_id = fields.Many2one('library.subject', string='subject name')
