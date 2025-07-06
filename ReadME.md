A food delivery platform where customers can order menu items from various restaurants.
Setup Instructions

1. Clone the repository
   In powershell
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2. Venv
   python -m venv venv
   PS> .\venv\Scripts\activate
3. Install dependencies
   pip install -r requirements.txt
4. Setup environment variables
   SECRET_KEY='your-secret-key'
   DEBUG=True
   DATABASE_URL='postgres://admin:password@localhost:5432/yourdbname'
5. Migrations
   python manage.py migrate
   python manage.py createsuperuser
6. Run the server
   python manage.py runserver

Open your browser and go to: http://127.0.0.1:8000/admin/
