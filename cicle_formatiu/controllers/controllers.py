# -*- coding: utf-8 -*-
# from odoo import http


# class Batoi(http.Controller):
#     @http.route('/batoi/batoi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/batoi/batoi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('batoi.listing', {
#             'root': '/batoi/batoi',
#             'objects': http.request.env['batoi.batoi'].search([]),
#         })

#     @http.route('/batoi/batoi/objects/<model("batoi.batoi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('batoi.object', {
#             'object': obj
#         })

