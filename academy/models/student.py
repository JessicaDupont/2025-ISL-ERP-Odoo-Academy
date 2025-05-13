# 1. Imports
from odoo import models, fields

# 2. Classe avec _name, _description, _order
class AcademyStudent(models.Model):
    _name = "academy.student"
    _description = "Élève ou étudiant"

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)

    # 3.2. dates / datetime

    # 3.3. relations
    partner_id = fields.Many2one('res.partner',
                                 string="Fiche contact",
                                 required=True,
                                 ondelete='cascade')

    # 3.4. calculés
    name = fields.Char(related='partner_id.name', store=False, readonly=True)
    email = fields.Char(related='partner_id.email', store=False, readonly=True)

    # 3.5. techniques
    active = fields.Boolean(default=True)

    # 4. Contraintes SQL

    # 5. Méthodes
    # 5.1. calculs (@api.depends)

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)

    # 5.4. @onchange