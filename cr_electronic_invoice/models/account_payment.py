from odoo import models, fields


class PaymentMethods(models.Model):
    _inherit = "payment.method"
    _name = "payment.methods"
    _description ='payment methods'

    # ==============================================================================================
    #                                          PAYMENT METHODS
    # ==============================================================================================
    notes = fields.Text()
