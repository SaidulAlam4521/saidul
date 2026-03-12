{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Library',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library_borrow_view.xml',
        'views/library_category_view.xml',
        'views/menu.xml',
        'data/library_data.xml',
        'wizard/wizard_checkout_view.xml',
    ],
    'installable': True,
}