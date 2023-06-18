from odoo import api, fields, models


class ProductExtraAttributes(models.Model):
    _name = "product.extra.attributes"
    _description = "Product Extra Attributes just as label on the ecommerce website"
    _order = "sequence,id"

    name = fields.Char()
    sequence = fields.Integer()
    value_ids = fields.One2many("product.extra.attributes.value", "attribute_id", "Values")


class ProductExtraAttributesValue(models.Model):
    _name = "product.extra.attributes.value"
    _description = "Product Extra Attributes' value"

    name = fields.Char()
    attribute_id = fields.Many2one("product.extra.attributes", "Attribute")


class ProductSpecLine(models.Model):
    _name = "product.spec.line"
    _description = "Each product's multiple attributes"

    attribute_id = fields.Many2one("product.extra.attributes", "Attribute")
    product_tmpl_id = fields.Many2one("product.template", "Product")
    value_ids = fields.Many2many(
        "product.extra.attributes.value", string="Values", domain="[('attribute_id', '=', attribute_id)]"
    )
