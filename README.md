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
