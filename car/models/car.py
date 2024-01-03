from odoo import models, fields

class Car(models.Model):
    _name = "car.car"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    production_date = fields.Date()
    brand = fields.Char()
    miles = fields.Integer()
    picture = fields.Binary()
    price = fields.Float()
    user_id = fields.Many2one('res.partner')

    def add_miles(self):
        self.miles += 1000

    def show_cars(self):
        action = {
            "type": "ir.actions.act_window",
            "res_model": "car.car",
            "view_mode": "tree,form"
        }
        return action

    def show_another(self):
        another_car = self.search([('id', '!=', self.id)], limit=1)
        action = {
            "type": "ir.actions.act_window",
            "res_model": "car.car",
            "view_mode": "form",
            "res_id": another_car.id,
        }
        return action

    def show_others(self):
        action = {
            "type": "ir.actions.act_window",
            "res_model": "car.car",
            "view_mode": "tree,form",
            "domain": [('id', '!=', self.id)],
        }
        return action
