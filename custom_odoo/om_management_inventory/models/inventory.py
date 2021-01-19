from odoo import fields, models, api, _


class Inventory(models.Model):
    _name = 'product.inventory'
    _description = 'product.inventory'

    product_id = fields.Many2one('product.manager', string='Product')
    date = fields.Date(String='EXP')
    amount = fields.Integer(string='Amount')

