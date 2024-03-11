{
    'name': 'World Clock',
    'author': 'Angelo Admin',
    'category': 'Application',
    'summary': 'World Clock',
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
