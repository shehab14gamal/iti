from  odoo import models,fields


class HrEmployssInherit(models.Model):


    _inherit = "hr.employee"

    national_id = fields.Char()