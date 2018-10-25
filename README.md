# ENV Virtual
    mkvirtualenv pico_placa

# Install Dependencies 
    pip install -r requirements.txt
    
# Create Migrations Empty
    python manage.py migrate

# Audit Test
    coverage run --source='.' manage.py test apps.pico_placa
    coverage report


