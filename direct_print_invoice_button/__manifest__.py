{
    'name': 'Direct Print Invoice Button',
    'version': '19.1.500', # ارفع الإصدار لضمان التحديث
    'category': 'Accounting',
    'price': 5.00,
    'currency': 'EUR',
    'license': 'OPL-1',
    'author': 'Shidoo-tech',
    'depends': ['account'],
    'data': [
        'views/button_view.xml', # تأكد أن الاسم يطابق ملف الـ XML تماماً
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'application': False,
    'auto_install': False, # إضافة اختيارية لضمان عدم التثبيت التلقائي
}
