===============================
setup.py and developer installs
===============================

Generally Python installs and deployments are a bit of a mess.
Not an unusable mess, but compared to the usually simple and
clear headed methods that most Python code provides, the morass of
setuptools, distutils, distribute, pip, easy_install and dist2 is 
... lacking.

Anyway, I used to ignore most of it.  Eggs where an abvstraciton too far
and so I tried to avoid them.  If I was developing I generally used softlinks in site-packages back to my actual code.  This worked quite nicely - code would run on my system, and would 


Virtualenv wolves many of the reasons for using eggs (ability to run multiple versions of code on same system) so combining the two tends to run into problems


Current situation
-----------------

I want to use namespaced packages
I want to use setup.py develop 




http://mail.python.org/pipermail/distutils-sig/2005-August/004970.html
"""This is why it's preferable to use 
the documented approach of listing namespace packages in setup(), and 
always using empty __init__.py files for namespace packages."""


What does work:

0. Create a clean venv, do setup.py develop for each namespaced package

0.1 create a clean venv, do setup.py develop for one namespaced package,
    do -e git+git using requirements file (which is git clone and then 
    setup.py develop anyway)

0.2 create clean venv and do 

What I cannot do through pip - install code not yet checked in.


Hacks

1. do a clean install, and then "manually" apply setup.py develop.
   this means create a  file rhaptos2.common.egg-link ::


     /usr/home/pbrian/src/rhaptos2.common
     .

   

   and adjust eay_install.pth sucvh that::

     ./pip-1.2.1-py2.7.egg            
     /usr/home/pbrian/src/rhaptos2.user
     /usr/home/pbrian/src/rhaptos2.common
     ./unittest_xml_reporting-1.4.1-py2.7.egg




What does NOT work

1. Create a clean venv and then setup.py develop, where I am running on 
   rhaptos2.user and that install_requires = rhaptos2.common

   ::

   rhaptos2.common-0.0.18-py2.7.egg 
   rhaptos2.user.egg-link

    >>> import rhaptos2.common
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: No module named common
    >>> import rhaptos2.user
    Traceback
    ...
    ImportError: No module named common
    >>> 
