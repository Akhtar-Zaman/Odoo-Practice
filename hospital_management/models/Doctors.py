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

    # doctor_list = []
    # def khan(self):
    #     self.doctor_list.clear()
    #     self.doctor_list.append(self.id)

    #     return self.doctor_list


    def Patient_Appointments(self):
        print("####################################", self.khan())
     
        return {
            'name': "Appointments",
            'type': "ir.actions.act_window",
            'res_model': "hospital.patients",
            'view_mode': "tree,form",
            #'domain': ['&', ('pat_doctor','=', self.id),('appointment_date','=',date.today())],
            'domain': [('pat_doctor','=', self.id)],
        }


############################################################################################
class purchasefilter(models.TransientModel):
    _name = 'patients.filter'

    date_from = fields.Date("From")
    date_to = fields.Date("To")  
 

    def patients_filter(self):

        # a = []
        # b = []

        # kk = self.env['hospital.patients'].search([ '&', ('appointment_date', '>=', self.date_from), ('appointment_date', '<=', self.date_to)])
        # dd = self.env['hospital.patients'].search([('pat_doctor','=', 1)])

        # for i in kk:
        #     b.append(i.id)

        # for i in dd:   
        #     a.append(i.id)
        
        # list1_as_set = set(a)
        # intersection = list1_as_set.intersection(b)
        # intersection_as_list = list(intersection)
        return {
            'name': "Patient filter",
            'type': "ir.actions.act_window",
            'res_model': "hospital.patients",
            'view_mode': "tree,form",
            #'domain': [('id','in', intersection_as_list)],
            'domain': [ '&', ('appointment_date', '>=', self.date_from), ('appointment_date', '<=', self.date_to)],
        }
        
        
