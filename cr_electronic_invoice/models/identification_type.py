from odoo import models, fields


class IdentificationType(models.Model):
    _name = "identification.type"
    _description ='identification.type'

    # ==============================================================================================
    #                                          IDENTIFICATION TYPE
    # ==============================================================================================

    code = fields.Char(
        help='Identification related code.'
    )
    name = fields.Char(
        help='Identification code name.'
    )
    notes = fields.Text(
        help='Identification notes.'
    )
