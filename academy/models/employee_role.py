from odoo import models, fields

class AcademyEmployeeRole(models.Model):
    _name = 'academy.employee.role'
    _description = "Rôle d’un employé"

    name = fields.Char(required=True)
    description = fields.Text()
    color = fields.Integer()
