# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BatoiAlumno(models.Model):
    _name = 'batoi.alumno'
    _description = 'Alumno de Batoi'
    _rec_name = 'nombre_completo'

    nombre_completo = fields.Char(string='Nombre y Apellidos', compute='_value_nombre')
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    modulo_ids = fields.Many2many(
        string='Modulos',
        comodel_name='batoi.modulo',
        relation='modulo_alumno',
        column1='modulo_id',
        column2='alumno_id',
    )
    
    @api.depends('nombre', 'apellidos')
    def _value_nombre(self):
        for record in self:
                if record.nombre and record.apellidos:
                    record.nombre_completo = f"{record.nombre} {record.apellidos}"
                else:
                    record.nombre_completo = ""