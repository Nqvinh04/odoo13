from odoo import models, fields, api, _


class Course(models.Model):
    _name = "academy.course"
    _description = "Academy Course"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Title", required=True)
    responsible_id = fields.Many2one('res.users', ondelete='set null',
                                     string="responsible", index=True)
    session_ids = fields.One2many('academy.session', 'course_id', string='Session')
