from unittest.result import failfast
from odoo import models, fields, api, _

class AccountTaxTemplate(models.Model):

    _name = 'account.tax.template'
    _description ='account.tax.template'

    # ==============================================================================================
    #                                          ACCOUNT TAX TEMPLATE
    # ==============================================================================================

    name = fields.Char(string="name")
    amount = fields.Float(string="amount")
    type_tax_use=fields.Char(string="type_tax_use")
    tax_group_id = fields.Char(string="tax_group_id")
    description=fields.Char(string="description")
    sequence= fields.Float(string="sequence")
    chart_template_id=fields.Char(string="chart_template_id")                      
    tax_code = fields.Char(string="Tax Code" )
    iva_tax_desc = fields.Char( string="VAT Tax Rate",default='N/A')
    iva_tax_code = fields.Char( string="VAT Rate Code", default='N/A')
    non_tax_deductible = fields.Boolean(string='Indicates if this tax is no deductible for Rent and VAT')

