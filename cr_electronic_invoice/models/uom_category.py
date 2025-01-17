from odoo import models, fields


class UoM(models.Model):
    _inherit = "uom.category"

    code = fields.Char()
