from odoo import models, fields, api
from odoo.exceptions import UserError

class ItiStudent(models.Model):
    _name = "iti.student"

    name = fields.Char(required=True)
    mobile = fields.Char()
    birth_date = fields.Date()
    basic_salary = fields.Float()
    bonus = fields.Float()
    salary = fields.Float(compute="compute_salary", store=True)
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

    ], default = 'applied')

    track_id = fields.Many2one("iti.track")
    is_track_open = fields.Boolean(related="track_id.is_open")
    skills_ids = fields.Many2many("iti.skills")
    @api.depends("basic_salary","bonus")
    def compute_salary(self):
        for rec in self:
            rec.salary = rec.basic_salary + rec.bonus


    def change_state(self):

        if  self.state == "applied":
            self.state = "first"
        elif self.state == "first" :
            self.state = "second"


    def acc(self):
        self.state = "accepted"


    def rejec(self):
        self.state ="rejected"


    @api.onchange("gender")
    def onchange_gender(self):
        if self.gender == "m":

            new_domain = []
        else:


          new_domain = [("is_open", "=", True)]

        return {
            "domain": {'track_id': new_domain},
            "warning":{
                  "title":"gender changed",
                  "message":"you have changed gender note that the salary & tracks available may be affected"
                      }

                }

    @api.constrains("mobile")
    def check_mobile(self):
         if len(self.mobile) != 11:
             raise UserError("enter 11 numbers")

    @api.model
    def create(self, vals):

        new_student = super().create(vals)
        new_student.track_id.is_open = True

        return new_student


    def unlink(self):
        for rec in self:
            if rec.state != "applied":
                raise UserError(f"can not delete student with state {rec.state}")
        return super().unlink()


    def write(self, vals):
        ss = self.search([('level', '=', 4)])

        for i in ss:
            print(i.track_id.track_name)

        return super().write(vals)



    _sql_constrains = [
        ('Valid Mobile', 'UNIQUE (mobile)', 'the number already exist')
    ]




















class ItiSkills(models.Model):

    _name ="iti.skills"
    name = fields.Char()





