from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    author_ids = fields.Many2many('res.partner', string='Authors')
    isbn = fields.Char('ISBN')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    publication_date = fields.Date('Publication Date')
    pages = fields.Integer('Number of Pages')
    price = fields.Monetary('Price', currency_field='currency_id')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')
    ], default='draft')
    cover_image = fields.Image('Cover Image')
    description = fields.Text('Description')
    borrowing_ids = fields.One2many('library.borrowing', 'book_id', string='Borrowing History')
    message_follower_ids = fields.Many2many('res.partner', 'library_book_followers', string='Followers')
    message_ids = fields.One2many('mail.message', 'res_id', domain=[('model', '=', 'library.book')], string='Messages')