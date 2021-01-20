from odoo import fields, models, api, _


class Inventory(models.Model):
    _name = 'product.inventory'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Product Inventory'

    product_id = fields.Many2one('product.manager', string='Product')
    date = fields.Date(string='EXP', default=fields.Date.context_today, track_visibility='always')
    dvt = fields.Char(default='Thùng', string="Quy Cách")
    amount = fields.Integer(string='Amount')


