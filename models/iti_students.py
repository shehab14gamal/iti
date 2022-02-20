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
    state = fields.Selection([
        ('applied',"Applied"),
        ('first',"Pass first interview"),
        ('second',"Pass second interview"),
        ('accepted',"Accepted"),
        ('rejected',"Rejected")

    ])
    @api.model
    def create(self, vals):
       new_student = super().create(vals)
       new_student.track_id.is_open = True
       return new_student

    def change_state(self):
        if self.state == False:
         self.state = "applied"
        elif  self.state == "applied":
            self.state = "first"
        elif self.state == "first" :
            self.state = "second"
    def acc(self):
        self.state = "accepted"
    def rejec(self):
        self.state ="rejected"
    track_id = fields.Many2one("iti.track")
    is_track_open = fields.Boolean(related="track_id.is_open")
    skills_ids = fields.Many2many("iti.skills")

    @api.onchange("gender")
    def onchange_gender(self):
        if self.gender == "m":
            self.salary = 10000
            new_domain = []
        else:
          self.salary = 5000

          new_domain = [("is_open", "=", True)]

        return {
            "domain": {'track_id': new_domain},
            "warning":{
                  "title":"gender changed",
                  "message":"you have changed gender note that the salary & tracks available may be affected"
                      }




                }


class ItiSkills(models.Model):

    _name ="iti.skills"
    name = fields.Char()





