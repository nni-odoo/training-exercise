from odoo import api, fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    age = fields.Integer("Age")
