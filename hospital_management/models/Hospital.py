from odoo import models, fields, api, _



class HospitalManagement(models.Model):
    _name = 'hospital.management'


    hos_name = fields.Char('Name')
    hos_mobile = fields.Integer('Phone Number')
    hos_email = fields.Char('Email')
    hos_address = fields.Char('Address')