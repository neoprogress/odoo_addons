from odoo import models, fields

class Account(models.Model):
    _name = 'module.account'
    _description = 'Account Model'

    name = fields.Char(string='Name', required=True)
    account_type = fields.Selection([
        ('virtual', 'Virtual'),
        ('cash', 'Cash'),
        ('mobile_money', 'Mobile Money'),
        ('online', 'Online'),
        ('bank', 'Bank'),
    ], string='Account Type', required=True)
    bank_details = fields.Text(string='Bank Details')

    # Other fields as per your requirements
