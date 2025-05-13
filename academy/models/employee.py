# 1. Imports
from odoo import models, fields

# 2. Classe avec _name, _description, _order
class AcademyEmployee(models.Model):
    _name = 'academy.employee'
    _inherits = {'hr.employee': 'employee_id'}
    _description = 'Employé Académie'

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)

    # 3.2. dates / datetime

    # 3.3. relations
    employee_id = fields.Many2one('hr.employee', 
                                  required=True, 
                                  ondelete="cascade")
    role_ids = fields.Many2many('academy.employee.role', 
                                string="Rôles")
    
    # 3.4. calculés

    # 3.5. techniques

    # 4. Contraintes SQL

    # 5. Méthodes
    # 5.1. calculs (@api.depends)

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)

    # 5.4. @onchange