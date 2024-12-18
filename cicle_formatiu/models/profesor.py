# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BatoiProfesor(models.Model):
    _name = 'batoi.profesor'
    _description = 'Profesor de Batoi'
    _rec_name = 'nombre_completo'

    nombre_completo = fields.Char(string='Nombre y Apellidos', compute='_value_nombre')
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    modulo_ids = fields.One2many(
        string='Modulos',
        comodel_name='batoi.modulo',
        inverse_name='profesor_id',
    )
    
    @api.depends('nombre', 'apellidos')
    def _value_nombre(self):
        for record in self:
                if record.nombre and record.apellidos:
                    record.nombre_completo = f"{record.nombre} {record.apellidos}"
                else:
                    record.nombre_completo = ""