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
    pat_disease = fields.Many2one('hospital.doctor.category', string="Disease")


    ####----------- Patients Appointments ------------####################

    

    pat_doctor = fields.Many2one('hospital.doctors', string="Doctor")
    appointment_date = fields.Date('Appointment Date')

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
        if val['pat_address']:
            result = super(HospitalPateient, self).create(val)
        else:
            val['pat_address'] = "House: 20/15, Tolarbag, Mirpur-01"
            result = super(HospitalPateient, self).create(val) 

        return result


    def write(self, val):
        if val['pat_address']:
            result = super(HospitalPateient, self).write(val)
        else:
            val['pat_address'] = "Deleted"
            result = super(HospitalPateient, self).write(val) 

        return result



#########################################################################################

class purchasefilter(models.TransientModel):
    _name = 'patients.filter'

    date_from = fields.Date("From")
    date_to = fields.Date("To")    

    def patients_filter(self):

        return {
            'name': "purchase filter",
            'type': "ir.actions.act_window",
            'res_model': "purchase.order",
            'view_mode': "tree,form",
            #'domain': [('id','in', intersection_as_list)],
        }