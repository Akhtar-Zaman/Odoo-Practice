from odoo import models, fields, api, _



class DoctorsCategory(models.Model):
    _name = 'hospital.doctor.category'
    _rec_name = 'hdc_name'


    hdc_name = fields.Char('Category')
    hdc_doctor = fields.One2many('hospital.doctors', 'doc_category', string="Department")

    