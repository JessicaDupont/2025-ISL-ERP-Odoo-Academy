# 1. Imports
from odoo import models, fields

# 2. Classe avec _name, _description, _order
class AcademyStaff(models.Model):
    _name = 'academy.staff'
    _description = "Membre du personnel administratif"

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)
    job_title = fields.Char(string="Fonction")
    active = fields.Boolean(default=True)

    # 3.2. dates / datetime

    # 3.3. relations
    user_id = fields.Many2one('res.users', string="Utilisateur", required=True, ondelete='cascade', domain="[('share', '=', False)]", help="L'utilisateur lié à ce membre du staff.")

    # 3.4. calculés

    # 3.5. techniques

    # 4. Contraintes SQL

    # 5. Méthodes
    # 5.1. calculs (@api.depends)

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)

    # 5.4. @onchange