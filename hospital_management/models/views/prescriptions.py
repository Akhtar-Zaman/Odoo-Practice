from odoo import models, fields, api, _


class DoctorsPrescription(models.Model):
    _name = 'doctors.prescription'


    name = fields.char('Medicine Name')