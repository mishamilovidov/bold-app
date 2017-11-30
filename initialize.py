from django.core import management
from django.db import connection
import os, os.path, sys

# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'boldapp.settings'
import django
django.setup()

# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")

# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')

# imports for our project
from django.contrib.auth.models import User
from boldapp.models import Equipment, Manufacturer, Department

admin = User()
admin.username = 'admin'
admin.set_password('password')
admin.first_name = 'admin'
admin.last_name = 'user'
admin.is_active = True
admin.is_superuser = True
admin.is_staff = True
admin.save()

greg = User()
greg.username = 'greg'
greg.set_password('password')
greg.first_name = 'greg'
greg.last_name = 'user'
greg.is_active = True
greg.is_superuser = True
greg.is_staff = True
greg.save()

misha = User()
misha.username = 'misha'
misha.set_password('password')
misha.first_name = 'misha'
misha.last_name = 'user'
misha.is_active = True
misha.is_superuser = True
misha.is_staff = True
misha.save()

ashton = User()
ashton.username = 'ashton'
ashton.set_password('password')
ashton.first_name = 'ashton'
ashton.last_name = 'user'
ashton.is_active = True
ashton.is_superuser = True
ashton.is_staff = True
ashton.save()




dell = Manufacturer()
dell.name = 'Dell'
dell.accountnumber = '12345'
dell.accountmanager = 'Mr. Dell'
dell.supportnumber = '801-555-1234'
dell.save()

apple = Manufacturer()
apple.name = 'Apple'
apple.accountnumber = '11111'
apple.accountmanager = 'Tom Cook'
apple.supportnumber = '661-222-3321'
apple.save()

microsoft = Manufacturer()
microsoft.name = 'Microsoft'
microsoft.accountnumber = '00000-1'
microsoft.accountmanager = 'Bill Gates'
microsoft.supportnumber = '999-999-9876'
microsoft.save()


accounting = Department()
accounting.name = 'Accounting'
accounting.supervisor = 'Mr. Bean'
accounting.phonenumber = '801-111-2222'
accounting.save()

finance = Department()
finance.name = 'Finance'
finance.supervisor = 'Mr. Bond'
finance.phonenumber = '801-555-1111'
finance.save()

marketing = Department()
marketing.name = 'Marketing'
marketing.supervisor = 'Mario'
marketing.phonenumber = '801-777-7777'
marketing.save()

equipment = Equipment()
equipment.name = 'MacBook Pro'
equipment.organizationaltag = 'TAG-1234'
equipment.description = 'Way overpriced, but looks nice.'
equipment.type = 'laptop'
equipment.manufacturer = apple
equipment.manufacturerpartnum = '11111111'
equipment.department = marketing
equipment.officelocation = 'B-212'
equipment.user = misha
equipment.save()

equipment = Equipment()
equipment.name = 'Dell Alienware'
equipment.organizationaltag = 'TAG-999999'
equipment.description = 'Gaming Rig'
equipment.type = 'desktop'
equipment.manufacturer = dell
equipment.manufacturerpartnum = '3333-3333'
equipment.department = finance
equipment.officelocation = 'A-111'
equipment.user = greg
equipment.save()

equipment = Equipment()
equipment.name = 'Surface RT'
equipment.organizationaltag = 'TAG-7777'
equipment.description = "Microsoft's kind of iPad"
equipment.type = 'tablet'
equipment.manufacturer = microsoft
equipment.manufacturerpartnum = '4444-22222'
equipment.department = accounting
equipment.officelocation = 'C-333'
equipment.user = ashton
equipment.save()
