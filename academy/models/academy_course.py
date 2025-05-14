from odoo import api,fields,models

class AcademyCourse(models.Model):
    _name = "academy.course"
    _description = "Class given at this academy"

    name = fields.Char(string="Title")
    description = fields.Char(string="Course description")
    code = fields.Char(string="Code")
    given_this_year = fields.Boolean(string="Given this year")
    total_hours = fields.Float(string="Total hours")
    credits = fields.Float(string="Credits")

    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string="End date")

    section_id = fields.Many2one("academy.section", string="Section", required=True)
    levels_ids = fields.Many2many("academy.level", string="Level")