from odoo import fields, models


class Course(models.Model):
    _name = 'e_learning_app.course'
    _description = 'Course'

    school_name = fields.Char(string='School Name')
    level = fields.Selection([
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('tertiary', 'Tertiary')
    ], string="Level")
    academic_year = fields.Selection([
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th')
    ], string="Semester")
    semester = fields.Char(string='Semester')
    faculty = fields.Char(string='Faculty')
    department = fields.Char(string='Department')
    course_title = fields.Char(string='Course Title')
    course_code = fields.Char(string='Course Code')
