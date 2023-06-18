from odoo import fields, models

class Product(models.Model):
    _inherit = "product.template"

    product_spec_line_ids = fields.One2many("product.spec.line", "product_tmpl_id", "Product Spec Line")
