from odoo import api,fields,models
from odoo.exceptions import UserError, ValidationError

class AcademySection(models.Model):
    _name = "academy.section"
    _description = "A section regroups multiple courses and can be spread on multiple levels."
    _order = "name"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", help="Abbreviation, e.g. BIG for Bachelier en Informatique de Gestion")
    description = fields.Char(string="Description")
    degree = fields.Boolean(string="Delivers degree")
    degree_specification = fields.Selection(
        string="Type of degree",
        selection=[('certification','Certification'),
                    ('bachelor','Bachelor'),
                    ('master','Master'),
                    ('phd','Ph.D.')]
    )
    number_of_levels = fields.Integer(string="Number of levels", required=True, default=1, inverse="_inverse_number_of_levels")

    courses_ids = fields.One2many("academy.course", "section_id", string="Courses")
    levels_ids = fields.One2many("academy.level", "section_id", string="Levels")

    @api.model
    def create(self, vals):
        if vals.get("number_of_levels"):
            record = super().create(vals) 
            number_of_levels = record.number_of_levels
            for level in range(number_of_levels):
                vals_level = [{'name': f'Level {level + 1}', 'section_id': record.id}]
                new_level = self.env["academy.level"].create(vals_level)
        
        return record

    @api.depends("levels_ids")
    def _inverse_number_of_levels(self):
        for record in self:
            record.number_of_levels = 10