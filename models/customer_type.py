from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class CustomerPartner(models.Model):

    _name = "res.partner"
    _inherit = "res.partner"

    code = fields.Char('Code', required=True,  readonly=False , index=True, default='New')
    type_id = fields.Many2one('customer.type', string='Customer Type')

    _sql_constraints = [('code_uniq','UNIQUE (code, type_id)','Code must be unique.')]


    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('res.partner') or 'New'
        return super(CustomerPartner, self).create(vals)

class CustomerType(models.Model):

    _name = "customer.type"
    _description = 'Customer Type'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
    active_type = fields.Boolean('Active Type', default=True)