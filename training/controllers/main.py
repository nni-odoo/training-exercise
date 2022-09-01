# -*- coding: utf-8 -*-
import datetime
from odoo import http, api, SUPERUSER_ID
from odoo.http import request
import json

class Controllers(http.Controller):

    @http.route('/hello', type='http')
    def hello(self, **kw):
        return "Hello, World!"

    @http.route('/hello_json', type='json')
    def hello_json(self, **kw):
        return json.dumps({"data": "Hello, World!"})

    @http.route("/sale_total")
    def sale_total(self, date=None, **kw):
        if request.httprequest.method == "POST":
            return request.redirect('/total/' + date)
        sales = request.env['sale.order'].search([])
        return "%s" % sum(sales.mapped('amount_total'))

    @http.route("/total/<string:date>")
    def sale_total_at_date(self, date, **kw):
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        sales = request.env['sale.order'].search([('date_order', '<=', parsed_date)])
        return "%s" % sum(sales.mapped('amount_total'))

    @http.route('/index')
    def index(self, **kw):
        return request.render("training.total_amount")
