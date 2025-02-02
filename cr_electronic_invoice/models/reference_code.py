
from odoo import models, fields


class ReferenceCode(models.Model):
    _name = "reference.code"
    _description ='reference.code'

    active = fields.Boolean(
        default=True
    )
    code = fields.Char()
    name = fields.Char()
