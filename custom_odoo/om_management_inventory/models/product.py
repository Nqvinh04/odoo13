from odoo import models, fields, api, _


class Product(models.Model):
    _name = 'product.manager'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Product Manager'

    name = fields.Char(string='Product Name', index=True, required=True)
    amount = fields.Integer(string='Amount', required=True)
    price = fields.Float(string='Price')
    dvt = fields.Selection([
        ('gói', 'Gói'),
        ('thùng', 'Thùng'),
    ], default='gói', string="Specifications")
    list_price = fields.Float(string='Total Price')
