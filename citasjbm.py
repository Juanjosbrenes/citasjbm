# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class citasjbm(models.Model):
	_name = 'citasjbm.citas'
	
	orden = fields.Char()
	fecha = fields.Char()
	cita = fields.Text()
	autor = fields.Char()