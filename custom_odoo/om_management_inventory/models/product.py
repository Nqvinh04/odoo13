from odoo import models, fields, api,tools, _


class Product(models.Model):
    _name = 'product.manager'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Product Manager'

    name = fields.Char(string='Tên Sản Phẩm', index=True, required=True, track_visibility='always')
    amount = fields.Integer(string='Số Lượng ', required=True, track_visibility='onchange')
    price = fields.Float(string='Giá/Gói', track_visibility='always')
    dvt = fields.Char(default='Gói', string="Quy Cách", track_visibility='always')
    inventory_ids = fields.One2many('product.inventory', 'product_id')
    product_variant_count = fields.Integer('Variant Count', related='product_tmpl_id.product_variant_count')
    type = fields.Selection([
        ('product', 'Storable Product'),
        ('consu', 'Consumable'),
        ('service', 'Service')
    ], string='Product Type', default='consu')
    default_code = fields.Char('Internal Reference', index=True)
    qty_available = fields.Integer(
        'Quantity On Hand', compute='_compute_quantities',
        digits='Product Unit of Measure', compute_sudo=False
    )
    image_1920 = fields.Image("Image", compute='_compute_image_1920', inverse='_set_image_1920')

    image_variant_1920 = fields.Image("Variant Image", max_width=1920, max_height=1920)
    image_variant_1024 = fields.Image("Variant Image 1024", related="image_variant_1920", max_width=1024,
                                      max_height=1024, store=True)
    # image_512 = fields.Image("Image 512", compute='_compute_image_512')
    # image_256 = fields.Image("Image 256", compute='_compute_image_256')
    # image_128 = fields.Image("Image 128", compute='_compute_image_128')
    can_image_1024_be_zoomed = fields.Boolean("Can Image 1024 be zoomed", compute='_compute_can_image_1024_be_zoomed')

    product_tmpl_id = fields.Many2one(
        'product.template', 'Product Template',
        auto_join=True, index=True, ondelete="cascade")

    @api.depends('image_variant_1920', 'image_variant_1024')
    def _compute_can_image_variant_1024_be_zoomed(self):
        for record in self:
            record.can_image_variant_1024_be_zoomed = record.image_variant_1920 and tools.is_image_size_above(record.image_variant_1920, record.image_variant_1024)

    def _compute_image_1920(self):
        """Lay hinh anh tu mau neu khong co hinh anh nao dat tren bien the"""
        for record in self:
            record.image_1920 = record.image_variant_1920 or record.product_tmpl_id.image_1920

    def _set_image_1920(self):
        for record in self:
            if (
                # Chúng tôi đang cố gắng xóa một hình ảnh mặc dù nó chưa được đặt,
                # thay vào đó hãy xóa nó khỏi mẫu.
                not record.image_variant_1920 and not record.image_variant_1920 or
                    # Chúng tôi đang cố gắng thêm một hình ảnh, nhưng hình ảnh mẫu chưa được đặt,
                    # hãy viết trên mẫu đó.
                record.image_variant_1920 and not record.image_variant_1920 or
                    # Chỉ có một biến thể duy nhất, luôn ghi trên bản mẫu.
                self.search_count([
                    ('product_tmpl_id', '=', record.product_tmpl_id.id),
                    ('active', '=', True),
                ]) <= 1
            ):
                record.image_variant_1920 = False
                record.product_tmpl_id.image_1920 = record.image_1920
            else:
                record.image_variant_1920 = record.image_1920

    def action_update_quantity_on_hand(self):
        return self.product_tmpl_id.with_context(default_product_id=self.id, create=True).action_update_quantity_on_hand()

    def action_update_quantity_on_hand(self):
        advanced_option_groups = [
            'om_management_inventory.group_stock_multi_locations',
            'om_management_inventory.group_production_lot',
            'om_management_inventory.group_tracking_owner',
            'om_management_inventory.group_stock_packaging',
        ]
        if (self.env.user.user_has_groups(','.join(advanced_option_groups))):
            return self.action_open_quants()
        else:
            default_product_id = self.env.context.get('default_product_id', len(self.product_variant_ids) == 1
                                                      and self.product_variant_id.id)
            action = self.env["ir.actions.actions"]._for_xml_id("om_management_inventory.action_change_product_quantity")
            action['context'] = dict(
                self.env.context,
                default_product_id=default_product_id,
                default_product_tmpl_id=self.id
            )
            return action





