{
    'name': 'World Clock',
    'author': 'Angelo Admin',
    'category': 'Application',
    'summary': 'World clock - 3',
    'description': """
        World Clock
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/wc_main_views.xml',
        'views/wc_menu_views.xml',
    ],
    'installable': True,
    'application': True
}
