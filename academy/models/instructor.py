# 1. Imports
from odoo import models, fields

# 2. Classe avec _name, _description, _order
class Instructor(models.Model):
    _name = 'academy.instructor'
    _description = 'Instructor'

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)
    active = fields.Boolean(default=True)

    # 3.2. dates / datetime

    # 3.3. relations
    user_id = fields.Many2one('res.users', string="Utilisateur", required=True, ondelete='cascade')

    # 3.4. calculés

    # 3.5. techniques

    # 4. Contraintes SQL

    # 5. Méthodes
    # 5.1. calculs (@api.depends)

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)

    # 5.4. @onchange