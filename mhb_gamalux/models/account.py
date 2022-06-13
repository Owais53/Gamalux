from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    paid_by_journal = fields.Char(compute='get_payment_journal')
    sale_tax_no = fields.Char()

    def get_payment_journal(self):
        for rec in self:
            move_id = self.env['account.move'].search([('ref','=',rec.name)])
            payment = self.env['account.payment'].search([('move_id','=',move_id.id)])
            rec.paid_by_journal = payment.journal_id.name

class customer(models.Model):
    _inherit = "res.partner"

    strn = fields.Char()
    ntn = fields.Char()
    cnic = fields.Char()