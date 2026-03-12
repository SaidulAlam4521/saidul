from odoo import models, fields

class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Book Category'

    name = fields.Char('Category Name', required=True)