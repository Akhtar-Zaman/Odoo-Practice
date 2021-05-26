from odoo import models, fields, api, _



class HospitalMedicines(models.Model):
    _name = 'hospital.medicines'
    _rec_name = 'mdcn_name'

    mdcn_image = fields.Binary(string='Image', attachment=True)
    mdcn_name = fields.Char('Name')
    mdcn_type = fields.Char('Type')
    mdcn_group = fields.Char('Group')
    mdcn_price = fields.Integer('Price')

    mdcn_description = fields.Text('Description')