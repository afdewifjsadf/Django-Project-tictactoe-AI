# django-tictactoe-AI
1. Clone this repository `git clone https://github.com/afdewifjsadf/django-tictactoe-AI.git`
2. Change directory `cd django-tictactoe-AI`
3. Virtualenv `virtualenv env` 
4. Activate virtualenv `env\Scripts\activate`
5. Install requirements `pip install -r requirements.txt`
6. Change directory `cd django48_1_5`
8. Run server `python manage.py runserver`

## reset-password setting
add Email and Password at `.\django-tictactoe-AI\django48_1_5\django48_1_5\settings.py`,
Email is lesssecure -> https://myaccount.google.com/lesssecureapps
```
EMAIL_HOST_USER = '** eamil **'
EMAIL_HOST_PASSWORD = '** password email **'
```
---
edit django at `.\django-tictactoe-AI\env\Lib\site-packages\django\contrib\admin\templates\registration\password_reset_email.html'
### Old
```
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
```
### New
```
{{ protocol }}://{{ domain }}{% url 'myapp:password_reset_confirm' uidb64=uid token=token %}
```
---
### Admin
Username: Admin.
Password: admin.
