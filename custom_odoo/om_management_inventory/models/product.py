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
    type = fields.Selection([
        ('product', 'Storable Product'),
        ('consu', 'Consumable'),
        ('service', 'Service')
    ], string='Product Type', default='consu')
    default_code = fields.Char('Internal Reference', index=True)
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
        auto_join=True, index=True, ondelete="cascade", required=True)

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



