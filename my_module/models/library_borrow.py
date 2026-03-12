from odoo import models, fields

class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Library Borrow'

    book_id = fields.Many2one('library.book', string='Book')
    borrower = fields.Many2one('res.partner', string='Borrower')
    borrow_date = fields.Date('Borrow Date', default=fields.Date.today)
    return_date = fields.Date('Return Date')