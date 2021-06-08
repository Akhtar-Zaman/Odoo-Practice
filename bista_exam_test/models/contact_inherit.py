from odoo import models, fields, api, _
from odoo.exceptions import UserError
import re


class ContactInheritView(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, values):
        if values['email']:
            match = re.match('^[_a-zA-Z0-9-]+(\.[_a-z0-9-]+)*@gmail+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', values['email'])
            if match:
                values['email'] = values['email'].lower()
                return super(ContactInheritView, self).create(values)
            else:
                raise UserError('Gmail Not Valid')

    def write(self, values):
        if 'email' in values.keys() and values['email']:
            match = re.match('^[_a-zA-Z0-9-]+(\.[_a-z0-9-]+)*@gmail+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', values['email'])
            if match:
                values['email'] = values['email'].lower()
                return super(ContactInheritView, self).write(values)
            else:
                raise UserError('Gmail Not Valid')