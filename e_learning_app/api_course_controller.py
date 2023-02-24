from odoo import http
from odoo.http import request


class CourseController(http.Controller):

    @http.route('/api/create_course', type='json', auth='public', methods=['POST'], csrf=False)
    def create_course(self, **kwargs):
        course = request.env['elearning.course'].create(kwargs)
        return course.read()

    @http.route('/api/update_course', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_course(self, **kwargs):
        course = request.env['elearning.course'].sudo().search([('id', '=', kwargs.get('id'))])
        course.write(kwargs)
        return course.read()

