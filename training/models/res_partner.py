from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    signature = fields.Binary()
