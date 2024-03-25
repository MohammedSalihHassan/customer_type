{   
 'name': 'customer type',
 'summary': """This module will add customer type with code""",
 'version': '14.0.1.0.0',
 'description': """add customer type with code""",
 'author': 'ALIAICT',
 'company': 'ALIA',
 'website': 'https://www.aliaict.com',
 'category': '',  
 'depends': ['base', 'contacts'],
 'license': 'AGPL-3',
 'data': [
       'security/ir.model.access.csv',
       'views/customer_type_view.xml',
       'data/customer_type_data.xml'
 ],
 'demo': [],
 'installable': True,
 'auto_install': False,
 'application': True,
}