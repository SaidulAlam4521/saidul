from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Book Title', required=True)
    isbn = fields.Char('ISBN')
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('unavailable', 'Unavailable'),
    ], default='available')
    borrow_ids = fields.One2many('library.borrow', 'book_id', string='Borrowed By')

    @api.depends('borrow_ids')
    def _compute_borrow_count(self):
        for book in self:
            book.borrow_count = len(book.borrow_ids)

    borrow_count = fields.Integer('Borrow Count', compute='_compute_borrow_count')

    def action_view_borrows(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Borrows',
            'res_model': 'library.borrow',
            'view_mode': 'list,form',
            'domain': [('book_id', '=', self.id)],
            'context': {'default_book_id': self.id},
        }

    def book_unavailable(self):
        self.state = 'unavailable'