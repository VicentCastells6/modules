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