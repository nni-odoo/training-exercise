from odoo import models
from odoo.exceptions import UserError

class Sale(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        if self.partner_id.sale_limit:
            if self.amount_total > self.partner_id.sale_limit:
                raise UserError(
                    "The total amount of the order is greater than the sale limit of the customer"
                )
        return super().action_confirm()
