from odoo import models, fields, api, _


class Session(models.Model):
    _name = 'academy.session'
    _description = 'OpenAcademy Session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    color = fields.Integer()
