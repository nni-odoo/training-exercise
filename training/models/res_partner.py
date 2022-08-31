from curses import KEY_CANCEL
from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.email = self.name.replace(' ', '_').lower() + "@odoo.com"
