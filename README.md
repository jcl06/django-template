Pull or download this repository only on your development environment or own machine.<br>
When you used pull delete .git directory inside the project directory then push to your own project repository.

<b>Requirements:</b>
 - Python 3.8 or later version
 - Do the following to install other requirements:
   - pip install pip --upgrade
   - pip install -r requirements.txt
 - Rename configs/settings/configuration_example.py into configuration.py and uncomment or fill any necessary configs.

Notes: If you can't install python_ldap in your machine install using pip. Install the python_ldap wheel from the <i>ldap wheels</i> folder by "pip install <i>python_ldap-3.4.0-xxx</i>". <b>Please delete the python_ldap wheel after installation.</b>
<br><br>
<b>Ensure you change/remove the ff</b>:
 - change the "django-template" in configs/celery.py on line 10
 - remove the path('', views.index, name='home') on core/urls.py if you already have your own home path 
 - change the SECRET_KEY on configuration.py with the encrypted secret key like SECRET_KEY = decrypt('encrypted key').
 - change the ENV on configuration.py to correct environment (dev, uat, prod)
 - change the PROJECT_NAME on configuration.py to your project name
 - change the BASE_PATH on configuration.py if your project hosted in a directory. For example, if installed at https://example.com/app/.
 - change the URL_PATH on configuration.py with the actual URL.
 - change the fqdn of your project in ALLOWED_HOSTS on configuration.py 
 - change or uncomment the REMOTE_AUTH_BACKEND on configuration.py if you want your project to be authenticated thru LDAP/AD.<br> 
   Then change the LDAP_ADDRESS, LDAP_USER, LDAP_PASS and other LDAPs configuration accordingly on configuration.py. Ensure the LDAP_PASS is encrypted.
 - Do "python managed.py collectstatic" when deploying in production
 
<b>Ensure all sensitive data keys or password are encrypted.</b>

