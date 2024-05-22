from odoo import http
from odoo.http import request

class School(http.Controller):

    @http.route('/school/student/',website=True,auth='public')
    def school_student(self,**kw):
        students = request.env['practice.student.profile'].sudo().search([])
        return request.render('my_practice_module.student_cont_template',{'students':students})

    @http.route('/school/hello',website=False, auth='public')
    def school_hello(self,**kw):
        return "Hello World from Karan !!"
