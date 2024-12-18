# -*- coding: utf-8 -*-

from odoo import models, fields


class BatoiCiclo(models.Model):
    _name = 'batoi.ciclo'
    _description = 'Ciclo Formativo de Batoi'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
    codigo = fields.Char(string='Codigo', required=True)
    descripcion = fields.Text(string='Descripcion del Ciclo')
    modulo_ids = fields.One2many(
        string='Modulos',
        comodel_name='batoi.modulo',
        inverse_name='ciclo_id',
    )