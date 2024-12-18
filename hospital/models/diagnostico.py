# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalDiagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Diagnostico del Medico'
    _order = 'fecha desc'

    medico_id = fields.Many2one(
        string='Medico',
        comodel_name='hospital.medico',
        ondelete='restrict',
    )
    paciente_id = fields.Many2one(
        string='Paciente',
        comodel_name='hospital.paciente',
        ondelete='restrict',
    )
    diagnostico = fields.Text(string='Diagnostico')
    fecha = fields.Datetime(string='Fecha del Diagnostico', default=fields.Datetime.now,)