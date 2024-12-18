# -*- coding: utf-8 -*-

from odoo import models, fields


class BatoiModulo(models.Model):
    _name = 'batoi.modulo'
    _description = 'Módulo de un Ciclo de Batoi'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
    codigo = fields.Char(string='Codigo', required=True)
    curriculo = fields.Text(string='Curriculo del Modulo')
    ciclo_id = fields.Many2one(
        string='Ciclo',
        comodel_name='batoi.ciclo',
        ondelete='cascade',
        required=True
    )
    profesor_id = fields.Many2one(
        string='Profesor',
        comodel_name='batoi.profesor',
        ondelete='restrict',
    )
    alumno_ids = fields.Many2many(
        string='Alumnos',
        comodel_name='batoi.alumno',
        relation='modulo_alumno',
        column1='alumno_id',
        column2='modulo_id',
    )