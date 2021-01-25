from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import clean_context


class ReplenishProduct(models.TransientModel):
    _name = 'replenish.product'
    _description = 'Product Replenish'

    product_id = fields.Many2one('product.Manager', string='Product', required=True)
    product_tmpl_id = fields.Many2one('product.template', string='Product Template', required=True)
    product_has_variants = fields.Boolean('Has Variants', default=False, required=True)
    # product_uom_category_id = fields.Many2one('uom.category', related='product_id.uom_id.category_id', readonly=True, required=True)
    product_uom_id = fields.Many2one('uom.uom', string='Unity of measure', required=True)
    quantity = fields.Integer(string='Quantity', default=1, required=True)
    date_planned = fields.Datetime(string='Scheduled Date', required=True,
                                   help="Date at which the replenishment should take place.")
