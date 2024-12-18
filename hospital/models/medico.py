# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalMedico(models.Model):
    _name = 'hospital.medico'
    _description = 'Medico del Hospital'
    _rec_name = 'nombre'
    _order = 'nombre'

    nombre = fields.Char(string='Nombre y Apellidos')
    num_colegiado = fields.Char(string='Numero de Colegiado')
    ejemplar_ids = fields.One2many(
        string='Diagnosticos',
        comodel_name='hospital.diagnostico',
        inverse_name='medico_id',
    )