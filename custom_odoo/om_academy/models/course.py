from odoo import models, fields, api, _


class Course(models.Model):
    _name = "academy.course"
    _description = "OpenAcademy Course"

    name = fields.Char(string="Title", required=True)
    description = fields.Char(string="Title", required=True)
