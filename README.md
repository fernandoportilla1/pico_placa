# ENV Virtual
    mkvirtualenv pico_placa

# Install Dependencies 
    pip install -r requirements.txt
    
# Migrations
    python manage.py migrate

# Styles And Js
    cd static/
    npm install

# Audit Test
    coverage run --source='.' manage.py test apps.vehicles
    coverage report


