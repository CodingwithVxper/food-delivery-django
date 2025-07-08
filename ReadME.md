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

API Setup & Usage
DRF Added
This project now includes Django REST Framework (DRF) for building and exposing API endpoints.

Base API URL
The base URL for the API is:
/api/
Exposed Models
The following models are currently available via the API:

Restaurant

Customer

MenuItem

Order

OrderItem

Browsable API Testing
Run the development server:
python manage.py runserver
Log in via the web UI at:
http://127.0.0.1:8000/accounts/login/
Visit the API root:
http://127.0.0.1:8000/api/
Use the browsable API to:

GET: View data

POST: Create new objects

PUT / PATCH: Update objects

DELETE: Remove objects
(You must be logged in to perform write operations.)

API Docs (via drf-spectacular)
If enabled, you can view live API documentation at:

Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/

Redoc: http://127.0.0.1:8000/api/schema/redoc/

Example Git Commit
After adding DRF + views + serializers:

git add .
git commit -m "feat: Add DRF API endpoints"
git push

API Filtering, Searching, and Ordering
You can filter, search, and order data using query parameters:

Filtering
Use field-based filters directly:

GET /api/restaurants/?cuisine=Italian

GET /api/restaurants/?owner=1

Searching
Use the search query parameter to match across searchable fields:

GET /api/restaurants/?search=burger

Ordering
Use the ordering parameter to sort results:

GET /api/restaurants/?ordering=name

GET /api/restaurants/?ordering=-id (descending order)

Pagination
API list endpoints are paginated by default.

Response includes: count, next, previous, and results keys.

Use ?page=<number> to navigate pages:

GET /api/restaurants/?page=2

Default page size is configured in settings.py under REST_FRAMEWORK['PAGE_SIZE'].

Permissions
We use a custom permission: IsOwnerOrReadOnly

Any authenticated user can view any object (GET).
Only the owner of the object can edit or delete it (PUT/PATCH/DELETE).

Example:

User A creates a restaurant.

User B can view it.

User B cannot modify/delete it.
Testing Instructions
To test permissions and filters:

1. Authentication
   Log in as User A and User B (create users if needed via Django admin or signup endpoint).

2. Test Ownership Permissions
   User A:

POST /api/restaurants/ – create a restaurant.

User B:

GET /api/restaurants/<id>/ – should succeed.

PUT/PATCH/DELETE /api/restaurants/<id>/ – should return 403 Forbidden.

POST /api/restaurants/ – should create a new object owned by User B.

PUT/PATCH/DELETE their own object – should succeed.

3. Test Filtering, Searching, Ordering
   GET /api/restaurants/?cuisine=Thai

GET /api/restaurants/?search=pizza

GET /api/restaurants/?ordering=-name

4. Test Pagination
   Ensure enough objects exist, then:

GET /api/restaurants/?page=1

GET /api/restaurants/?page=2
