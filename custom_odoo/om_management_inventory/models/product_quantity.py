from odoo import models, fields, api, _


class ProductQuantity(models.Model):
    _name = 'product.quantity'
    _description = 'Quantity in product'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.manager', string='Product')
    quantity = fields.Integer(string='Quantity', readonly=True)
    inventory_quantity = fields.Integer(string='Inventory Quantity')
    reserved_quantity = fields.Integer(string='Reserved Quantity', default=0, readonly=True,
                                       required=True)
    available_quantity = fields.Integer(string='Available Quantity')
    date = fields.Date(string='EXP', default=fields.Date.context_today, track_visibility='always')


