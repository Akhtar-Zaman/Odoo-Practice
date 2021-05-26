from odoo import models, fields, api, _
from odoo.exceptions import UserError




class HospitalPateient(models.Model):
    _name = 'hospital.patients'
    _rec_name = 'pat_name'

    pat_name = fields.Char('Name')
    pat_age = fields.Integer('Age')
    check = fields.Boolean('check')
    
    pat_disease = fields.Many2one('hospital.doctor.category', string="Disease")
    pat_doctor = fields.Many2one('hospital.doctors', string="Doctor")

    appointment_date = fields.Date('appointment date')



