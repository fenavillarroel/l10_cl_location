from odoo import fields, models, api

class ResCompany(models.Model):
    _inherit = 'res.company'
    
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
