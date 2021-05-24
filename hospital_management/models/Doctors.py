from odoo import models, fields, api, _
from datetime import date




class HospitalDoctors(models.Model):
    _name = 'hospital.doctors'
    _rec_name = 'doc_name'


    doc_image = fields.Binary('Image', attachment=True)
    doc_name = fields.Char('Name')
    doc_mobile = fields.Integer('Phone Number')
    doc_email = fields.Char('Email')
    doc_address = fields.Text('Address')


    doc_patients = fields.One2many('hospital.patients', 'pat_doctor', string="Patients")

    doc_category = fields.Many2one('hospital.doctor.category', string='Department')


    def Patient_Appointments(self):
        return {
            'name': "Appointments",
            'type': "ir.actions.act_window",
            'res_model': "hospital.patients",
            'view_mode': "tree,form",
            'domain': ['&', ('pat_doctor','=', self.id),('appointment_date','=',date.today())],
        }
