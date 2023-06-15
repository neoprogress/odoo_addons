from odoo import models, fields, api

class Transaction(models.Model):
    _name = 'module.transaction'
    _description = 'Transaction Model'

    movement_id = fields.Many2one('module.movement', string='Parent Movement', required=True)
    amount = fields.Float(string='Amount', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    conversion_rate = fields.Float(string='Conversion Rate')
    additional_details = fields.Text(string='Additional Details')

    # Compute field to calculate the converted amount
    converted_amount = fields.Float(string='Converted Amount', compute='_compute_converted_amount')

    @api.depends('amount', 'conversion_rate')
    def _compute_converted_amount(self):
        for record in self:
            record.converted_amount = record.amount * record.conversion_rate
