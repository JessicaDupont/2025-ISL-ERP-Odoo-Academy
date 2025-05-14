from odoo import api,fields,models
from odoo.exceptions import ValidationError

class AcademyLevel(models.Model):
    _name = "academy.level"
    _description = "A section can have multiple levels."
    
    name = fields.Char(string="Level", required=True)
    unique_level = fields.Boolean(string="Unique level", help="Tick this case if the section only has one level.")

    section_id = fields.Many2one("academy.section", string="Section", required=True)