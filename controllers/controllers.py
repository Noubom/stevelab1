# -*- coding: utf-8 -*-
# from odoo import http


# class SteveLab1(http.Controller):
#     @http.route('/steve_lab1/steve_lab1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/steve_lab1/steve_lab1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('steve_lab1.listing', {
#             'root': '/steve_lab1/steve_lab1',
#             'objects': http.request.env['steve_lab1.steve_lab1'].search([]),
#         })

#     @http.route('/steve_lab1/steve_lab1/objects/<model("steve_lab1.steve_lab1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('steve_lab1.object', {
#             'object': obj
#         })
