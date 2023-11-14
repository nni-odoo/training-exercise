# -*- coding: utf-8 -*-
import datetime
from odoo import http, SUPERUSER_ID
from odoo.http import request
import json

class Controllers(http.Controller):

    # Exercise 1.1 & 1.2
    @http.route(['/hello', '/hello/<string:name>'])
    def hello(self, name="world", **kw):
        return "Hello, %s!" % name

    # Exercise 1.3
    @http.route("/json_data", auth='none')
    def json_data(self, **values):
        headers = {'Content-Type': 'application/json'}
        body = {'x': 1, 'y': 2}

        return request.make_response(json.dumps(body), headers)

    # Exercise 1.4
    @http.route("/total/<string:date>")
    def sale_total_at_date(self, date, **kw):
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        sales = request.env['sale.order'].search([('date_order', '<=', parsed_date)])
        return "%s" % sum(sales.mapped('amount_total'))

    @http.route('/index')
    def index(self, **kw):
        return request.render("training.total_amount")

    # Exercise 2.1
    @http.route("/start")
    def start(self, **kw):
        vals = {'name': 'test', 'age': 20}
        return request.render("training.example_template", vals)

    # Exercise 2.2
    @http.route("/sale/<int:sale_id>")
    def sale(self, sale_id, **kw):
        sale = request.env['sale.order'].browse(sale_id)
        return request.render("training.sale_web", {'order': sale})

    @http.route('/create/partner', methods=['POST'], type='http', auth='public', website=True, csrf=False)
    def create_partner(self, name):
        request.env['res.partner'].sudo().create({'name': name})
