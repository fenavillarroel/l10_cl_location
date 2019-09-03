# -*- coding: utf-8 -*-
from odoo import http

# class L10ClLocation(http.Controller):
#     @http.route('/l10_cl_location/l10_cl_location/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10_cl_location/l10_cl_location/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10_cl_location.listing', {
#             'root': '/l10_cl_location/l10_cl_location',
#             'objects': http.request.env['l10_cl_location.l10_cl_location'].search([]),
#         })

#     @http.route('/l10_cl_location/l10_cl_location/objects/<model("l10_cl_location.l10_cl_location"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10_cl_location.object', {
#             'object': obj
#         })