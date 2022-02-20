from odoo import models, fields, api

class ItiStudent(models.Model):
    _name = "iti.student"
    name = fields.Char(required=True)
    birth_date = fields.Date()
    salary = fields.Float()
    address = fields.Text()
    gender = fields.Selection(
        [('m',"Male"),('f',"Female")]
    )
    military_certificate = fields.Binary()
    accepted = fields.Boolean()
    level = fields.Integer()
    image = fields.Binary()
    cv = fields.Html()
    login_time = fields.Datetime()
    track_id = fields.Many2one("iti.track")
    is_track_open = fields.Boolean(related="track_id.is_open")
    skills_ids = fields.Many2many("iti.skills")

    @api.onchange("gender")
    def onchange_gender(self):
        if self.gender == "m":
            self.salary = 10000
        else:
           self.salary = 5000


class ItiSkills(models.Model):

    _name ="iti.skills"
    name = fields.Char()





