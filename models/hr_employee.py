from odoo import fields, models, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    street = fields.Char(string='Calle',size=128)
    street2 = fields.Char(string='Calle2',size=128)
    zip = fields.Char(string='Código Postal',size=56)
    city = fields.Char(string='Ciudad',size=128)
    state_id = fields.Many2one('res.country.state','Comuna')
    id_provincia = fields.Many2one('res.country.provincias', 'Provincia')
    id_region = fields.Many2one('res.country.region', 'Región')

    @api.onchange('state_id')
    def onchange_state_id(self):

            prov = self.env['res.country.state'].search([('id','=',self.state_id.id)])
            self.id_provincia = prov.id_provincia
            self.city = prov.name
            reg = self.env['res.country.provincias'].search([('id','=',self.id_provincia.id)])
            self.id_region = reg.id_region
            self.country_id = prov.country_id
