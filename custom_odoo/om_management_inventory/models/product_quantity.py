from odoo import models, fields, api, _


class ProductQuantity(models.Model):
    _name = 'product.quantity'
    _description = 'Quantity in product'
    _rec_name = 'product_id'
