# Django first steps!

    # clone repo
    git clone https://github.com/pahaz/django_test1.git my-first-project-name
    cd my-first-project-name
    
    # install virtualenv
    pip install virtualenv  # easy_install virtualenv
    
    # make virtualenv
    virtualenv venv
    
    # activate venv
    venv\Scripts\activate  # windows
    . venv/bin/activate  # Linux, OS X
    
    # install requirements
    pip install -r requirements.txt
    
    # create db
    python manage.py migrate
    
    # run server
    python manage.py runserver_plus

# Step 1 #

 - `virtualenv .venv`, activate, `pip install -r requirements.txt`
 - `python manage.py startproject`
 - project structure (`manage.py`, `_project_v1_`, `_project_v1_/settings.py`, `_project_v1_/wsgi.py`, `_project_v1_/urls.py`)
 - `python manage.py runserver`
 - project settings (`DEBUG`, `INSTALLED_APPS`, `ROOT_URLCONF`, `WSGI_APPLICATION`, `DATABASES`, `TEMPLATES`, `TEMPLATES['DIRS']`)
 - write simple view `def index(request): return render(request, 'index.html')` in `urls.py`
 - add `_project_v1_/templates/index.html`, change settings `TEMPLATES['DIRS']`
 - install `django_debug_toolbar>=1.3.0`, `django_extensions>=1.5.2`, add to `INSTALLED_APPS`
 - show `debug-toolbar` features
 - show `python manage.py runserver_plus`
 - add static file `_project_v1_/static/robots.txt`, change settings `STATICFILES_DIRS`; tell about how to django gives static files, `'django.contrib.staticfiles'` 
 - show django admin interface; tell about User, Group, Permission models; overview of `INSTALLED_APPS`

# Step 2 #

 - tell about ORM, migrations
 - `python manage.py startapp`
 - app structure (`models.py`, `migrations`, `views.py`, `tests.py`, `admin.py`)
 - write simple `Model` (`class Entry(models.Model): title = models.CharField(max_length=200)`)
 - `python manage.py help`
 - `python manage.py makemigrations`, show `migrations/0001_initial.py`
 - `python manage.py migrate`
 - show `db.sqlite3` file (sqlite3 view)
 - `python manage.py shell`, `python manage.py shell_plus`
 - create models and show in `db.sqlite3` file
 - show models API, tell about `Manager`
 - write model with `ForeignKey`, `ManyToManyField` and `DateTimeField` (`Entry` with author and `Tags`)
 - show `python manage.py makemigrations` and tell about the new columns default values; show `migrations/0002_auto*.py`
 - show more model API; tell about `.save()` related objects 
 - show how to write simple script for work with `models.py` (`os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_project_v1_.settings"); from django.conf import settings`)

# Step 3 #

 - write `view.py`, function based views (FBV), good for read and understand, docorator concept.
 - write `urls.py`, url `include`
 - `Form`, `ModelForm`, `Widget`, form in templates, `csrf_token`, `clean()`
 - simple `admin.py`, `admin.site.register`
 - settings `LANGUAGE_CODE`, `TIME_ZONE`
 - rewrite `view.py`, class based views (CBV), [https://ccbv.co.uk/], bad for understand, mixin concept.
 - `request.user`, `AnonymousUser`

# Step 4 #
 - more `admin.py`
 - https://github.com/pahaz/django-steps/tree/master/_step_06 (encapsulate app logic), tell about override app logic (templates, templates tags/filters, template context processors, urls, view, decorator, mixin)
 - settings `TEMPLATE_CONTEXT_PROCESSORS`
 - tell how django processes a request: https://docs.djangoproject.com/en/dev/_images/middleware.svg
