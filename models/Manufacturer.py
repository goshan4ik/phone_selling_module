# -*- coding: utf-8 -*-

from odoo import models, fields


class Manufacturer(models.Model):
    _name = 'manufacturer'
    name = fields.Char()
    country = fields.Char()
