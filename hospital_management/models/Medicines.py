from odoo import models, fields, api, _



class HospitalMedicines(models.Model):
    _name = 'hospital.medicines'

    mdcn_image = fields.Binary(string='Image', attachment=True)
    mdcn_name = fields.Char('Meicine Name')
    mdcn_type = fields.Char('Medicine Type')
    mdcn_group = fields.Char('Medicine Group')
    mdcn_description = fields.Text('Description')