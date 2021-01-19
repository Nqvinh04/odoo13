from odoo import models, fields, api, _


class Product(models.Model):
    _name = 'product.manager'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Product Manager'

    name = fields.Char(string='Tên Sản Phẩm', index=True, required=True)
    amount = fields.Integer(string='Số Lượng ', required=True)
    price = fields.Float(string='Giá/Gói')
    dvt = fields.Char(default='Gói', string="Quy Cách")
    inventory_id = fields.One2many('product.inventory', 'product_id')
