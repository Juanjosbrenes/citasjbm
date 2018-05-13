# -*- coding: utf-8 -*-
from odoo import http

# class Citasjbm(http.Controller):
#     @http.route('/citasjbm/citasjbm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasjbm/citasjbm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasjbm.listing', {
#             'root': '/citasjbm/citasjbm',
#             'objects': http.request.env['citasjbm.citasjbm'].search([]),
#         })

#     @http.route('/citasjbm/citasjbm/objects/<model("citasjbm.citasjbm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasjbm.object', {
#             'object': obj
#         })