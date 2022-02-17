from odoo import models, fields

class ItiTrack(models.Model):
    _name = "iti.track"
    name = fields.Char()
    is_open = fields.Boolean()
