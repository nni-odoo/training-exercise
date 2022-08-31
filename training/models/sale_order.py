from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_items = fields.Integer("Total Items", compute="_compute_total_items")

    @api.depends('order_line.product_uom_qty')
    def _compute_total_items(self):
        for rec in self:
            rec.total_items = sum(rec.order_line.mapped('product_uom_qty'))
