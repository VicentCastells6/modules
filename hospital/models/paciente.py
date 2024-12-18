# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente del Hospital'
    _rec_name = 'nombre'
    _order = 'nombre'

    nombre = fields.Char(string='Nombre y Apellidos')
    sintomas = fields.Text(string='Sintomas')
    ejemplar_ids = fields.One2many(
        string='Diagnosticos',
        comodel_name='hospital.diagnostico',
        inverse_name='paciente_id',
    )