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

### Routes:

- List: `/restaurants/`
- Detail: `/restaurants/<id>/`
- Create: `/restaurants/create/`
- Update: `/restaurants/<id>/update/`
- Delete: `/restaurants/<id>/delete/`

### Features:

- Template-based layout using `base_generic.html`
- Success messages on create/update/delete
- Easy navigation across views

## Setup Instructions

git clone https://github.com/CodingwithVxper/food-delivery-django.git
cd myproj
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

I implemented a Django-based authentication system for my project, combining traditional login with Google OAuth2 login using django-allauth. I configured the .env file to securely manage sensitive credentials like the Google Client ID and Secret, and integrated social authentication into your login flow. I also added permission restrictions, ensuring that only authenticated users can access or modify certain views like update and delete for the Restaurant model. Class-based views were used throughout, and I implemented a confirmation page for deletions with CSRF protection.

1. Setting Up Google OAuth Credentials
   To enable Google login for this project:

Go to the Google Cloud Console.

Create a new OAuth 2.0 Client ID under Credentials.

Set the application type to Web application.

In Authorized Redirect URIs, add:

http://localhost:8000/accounts/google/login/callback/
After creating, copy the Client ID and Client Secret.

Then, update your local .env file with:

GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret
Restart the server after saving changes:

python manage.py runserver

2. Testing Login (Local + Google)
   Local Login:

Visit: http://localhost:8000/accounts/login/

Register or sign in with a username/password.

Google Login:

Visit: http://localhost:8000/accounts/google/login/

Or add a login button using:
<a href="{% provider_login_url 'google' %}">Login with Google</a>

3. Testing Permissions (Update/Delete)
   Create: Any logged-in user can create a restaurant.
   Update: Only users with is_staff=True can update any restaurant.
   Delete: Only the owner (creator) of a restaurant can delete it.

To test:
Log in as a regular user and try to update a restaurant → Access denied.
Log in as a staff user and try updating → Access granted.
Try deleting a restaurant you didn’t create → Access denied.
Delete your own restaurant → Should succeed.
