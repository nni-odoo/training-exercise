from odoo import fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    sale_limit = fields.Float()
