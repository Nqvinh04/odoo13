from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductChangeQuantity(models.TransientModel):
    _name = "change.product.qty"
    _description = "Change Product Quantity"

    product_id = fields.Many2one('product.manager', string='Product', required=True)
    product_tmpl_id = fields.Many2one('product.template', string='Template', required=True)
    product_variant_count = fields.Integer('Variant Count',
                                           related='product_tmpl_id.product_variant_count', readonly=True)
    new_quantity = fields.Integer(string='New Quantity On Hand', default=1,
                                  digits='Product Unit of Measure', required=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        self.new_quantity = self.product_id.qty_available

    @api.constrains('new_quantity')
    def check_new_quantity(self):
        if any(wizard.new_quantity < 0 for wizard in self):
            raise UserError(_('Quantity cannot be negative.'))

    def change_product_qty(self):
        print("Thanh Cong")
