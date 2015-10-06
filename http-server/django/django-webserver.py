#!/usr/bin/python

### Django ORM --  Object Relation Mapping
### Djanog Templates
## Hiteshs-MacBook-Air:django hitesha$ django-admin.py startproject learnpython
## cd learnpython
## manage.py runserver
# Hiteshs-MacBook-Air:learnpython hitesha$ ./manage.py runserver
# Performing system checks...

# System check identified no issues (0 silenced).

# You have unapplied migrations; your app may not work properly until they are applied.
# Run 'python manage.py migrate' to apply them.

# October 05, 2015 - 10:04:10
# Django version 1.8.5, using settings 'learnpython.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.

#./manage.py startapp msg
## Now update learnpython/setting.py and add msg in INSTALLED_APPS

# Hiteshs-MacBook-Air:learnpython hitesha$ ./manage.py shell
# Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from msg.models import Message
# >>> Message.objects.all()
# []
# >>> testmessage = Message(message="test message", username = "Test User")
# >>> testmessage.save()
# >>> Message.objects.all()
# [<Message: Message object>]
# >>> msgobjects = Message.objects.all()
# >>> msgobjects[0].message
# u'test message'
# >>> msgobjects[0].username
# u'Test User'
# >>> 



from django.db import models
class Musician(models.Model):
	first_name = models.CharField(max_length=50)
