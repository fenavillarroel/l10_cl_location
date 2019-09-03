from odoo import fields, models, api

class ResCountryProvincias(models.Model):
    _name = 'res.country.provincias'
    _description = "Res Country Provincias"
    _order = 'name asc'

    name = fields.Char(string='Nombre',size=128)
    code = fields.Char(string='Código',size=28) 
    id_region = fields.Many2one('res.country.region', 'Región')

