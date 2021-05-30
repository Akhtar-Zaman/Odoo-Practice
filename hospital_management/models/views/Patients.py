from odoo import models, fields, api, _
from odoo.exceptions import UserError



class HospitalPateient(models.Model):
    _name = 'hospital.patients'
    _rec_name = 'pat_name'

    pat_image = fields.Binary(string='Image', attachment=True)
    pat_name = fields.Char('Name')
    pat_mobile = fields.Integer('Phone Number')
    pat_email = fields.Char('Email')
    pat_address = fields.Text('Address')
    pat_bill = fields.Integer('Bill')
    pat_discountBill = fields.Integer('Discount', compute='discount_bill')
    appointment_date = fields.Date('Appointment Date')


    
    pat_disease = fields.Many2one('hospital.doctor.category', string="Disease")
    pat_doctor = fields.Many2one('hospital.doctors', string="Doctor")
    pat_medicine = fields.Many2many('hospital.medicines', string='Medicines')
    pat_medicine_price = fields.Integer(string='Price', compute='get_medicine_price')




    def doc(self):
        aa = self.env['hospital.doctors'].search([('id', '=', self.pat_doctor.id)])
        return aa.doc_name

    def get_medicine_price(self):
        
        total_medicine_price = 0
        aa = self.env['hospital.medicines'].search([('id', 'in', self.pat_medicine.ids)])
        for i in aa:
            total_medicine_price = total_medicine_price+i.mdcn_price

        self.pat_medicine_price = total_medicine_price



    @api.depends('pat_bill')
    def discount_bill(self):

        bb = (self.pat_bill*10)/100
        self.pat_discountBill = bb

    @api.onchange('pat_mobile')
    def pat_mobile_onchange(self):
        
        if self.pat_mobile and len(str(self.pat_mobile)) != 2:
            raise UserError(_("Phone Number is not VALID"))

    @api.model 
    def create(self, val):
        if not val['pat_address']:
            val['pat_address'] = 'House: 20/15, Tolarbag R/A, Mirpur-01, Dhaka-1216'

        return super(HospitalPateient, self).create(val)


    def write(self, val):
        if 'pat_address' in val.keys() and not val['pat_address']:
             val['pat_address'] = 'Deleted'

        return super(HospitalPateient, self).write(val)


    def Prescribe(self):
    
        return {
            'name': "Prescription",
            'type': "ir.actions.act_window",
            'res_model': "doctors.prescription",
            'view_mode': "form",
            'context': {'default_Patient_name': self.pat_name,
                        'default_Patient_email': self.pat_email,  
                        'default_Patient_doctor': self.doc(),  
            }         
        }



#########################################################################################

