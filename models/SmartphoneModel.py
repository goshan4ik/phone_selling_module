# -*- coding: utf-8 -*-

from odoo import models, fields


class SmartphoneModel(models.Model):
    _name = 'smartphone_model'
    name = fields.Char(index=True, required=True)
    manufacturer = fields.Many2one('manufacturer',
        ondelete='cascade', string="Manufacturer", index=True, required=True)
    release_year = fields.Integer(required=True)
    description = fields.Text()
