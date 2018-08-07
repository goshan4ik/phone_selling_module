# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Phone(models.Model):
    _inherit = 'product.template'
    manufacturer = fields.Many2one('manufacturer',  ondelete='cascade', string="Manufacturer",
                                   index=True, required=True,
                                   default=lambda self: self.env['manufacturer'].search([], limit=1))
    phoneModel = fields.Many2one('smartphone_model', ondelete='cascade', string="Model", index=True,
                                 required=True)
    name = fields.Char(compute="_onchange_name", store=True)

    state = fields.Selection([
        ('add_meta_data', 'General info'),
        ('avatar', 'Phone image'),
    ], default='add_meta_data')

    @api.multi
    @api.onchange('next_button')
    def onchange_my_button(self):
        for record in self:
            record.write({
                'state': 'avatar',
            })

    @api.onchange('manufacturer')
    def _campus_onchange(self):
        self.phoneModel = self.env['smartphone_model'].search([('manufacturer', '=', self.manufacturer.id)], limit=1)
        res = {}
        res['domain'] = {'phoneModel': [('manufacturer', '=', self.manufacturer.id)]}
        return res

    @api.depends('manufacturer', 'phoneModel')
    @api.multi
    def _onchange_name(self):
        for record in self:
            if not record.phoneModel:
                record.name = record.manufacturer.name
            else:
                record.name = record.manufacturer.name + ' ' + record.phoneModel.name

    @api.multi
    def next_btn(self):
        self.write({
            'state': 'avatar',
        })
        return {
            "type": "ir.actions.do_nothing",
        }
