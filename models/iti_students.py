from odoo import models, fields

class ItiStudent(models.Model):
    _name = "iti.student"
    name = fields.Char(required=True)
    birth_date = fields.Date()
    salary = fields.Float()
    address = fields.Text()
    gender = fields.Selection(
        [('m',"Male"),('f',"Female")]
    )
    accepted = fields.Boolean()
    level = fields.Integer()
    image = fields.Binary()
    cv = fields.Html()
    login_time = fields.Datetime()
    track_id = fields.Many2one("iti.track")
    is_track_open = fields.Boolean(related="track_id.is_open")
    skills_ids = fields.Many2many("iti.skills")


class ItiSkills(models.Model):

    _name ="iti.skills"
    name = fields.Char()





