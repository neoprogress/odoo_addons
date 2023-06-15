from odoo import models, fields

class Movement(models.Model):
    _name = 'module.movement'
    _description = 'Movement Model'

    source_account_id = fields.Many2one('module.account', string='Source Account')
    destination_account_id = fields.Many2one('module.account', string='Destination Account')
    amount = fields.Float(string='Amount', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    execution_date = fields.Date(string='Execution Date')
    label = fields.Char(string='Label')
    state = fields.Selection([
        ('planned', 'Planned'),
        ('partially_executed', 'Partially Executed'),
        ('completed', 'Completed'),
    ], string='State', default='planned')
    administrator_id = fields.Many2one('res.users', string='Administrator')

    # Other fields as per your requirements

class Account(models.Model):
    _name = 'module.account'
    _description = 'Account Model'

    name = fields.Char(string='Name')
    administrator_id = fields.Many2one('res.users', string='Administrator')

    # Other fields as per your requirements
