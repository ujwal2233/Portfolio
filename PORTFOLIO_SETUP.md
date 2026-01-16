# Beautiful Portfolio Website - Setup & Usage Guide

## Overview
Your portfolio website has been successfully updated to dynamically pull data from a Django database instead of using hardcoded values. This makes it easy to update your portfolio content without editing HTML files.

## What Was Done

### 1. **Created Django Models**
The following models have been created to store your portfolio data:

- **Profile**: Your personal information (name, title, bio, email, phone, location, social links)
- **Experience**: Your work experience history
- **Skill**: Your technical skills organized by category
- **Project**: Your portfolio projects
- **Certification**: Your professional certifications
- **Education**: Your educational background

### 2. **Updated Views**
All views now fetch data from the database and pass it to templates:
- `index.html` - Shows your profile and featured projects
- `about.html` - Displays your bio and education
- `skills.html` - Lists all your skills organized by category
- `projects.html` - Shows all your projects
- `experience.html` - Timeline of your work experience
- `certifications.html` - Your professional certifications
- `resume.html` - Complete resume preview
- `contact.html` - Contact information from your profile

### 3. **Registered Models in Admin**
All models have been registered in Django Admin for easy management.

## How to Access and Manage Your Data

### 1. **Create a Superuser (Admin Account)**
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 2. **Access Django Admin**
1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Go to: `http://localhost:8000/admin/`
3. Login with your superuser credentials

### 3. **Update Your Portfolio Data**
In the Django Admin, you'll see sections for:

#### **Profile**
- Edit your main profile with name, title, bio, contact info, and social media links

#### **Experience**
- Add, edit, or delete work experience entries
- Fields: Title, Company, Location, Start Date, End Date, Description, Is Current (checkbox)

#### **Skills**
- Add skills organized by category (Programming Language, Framework/Library, Database, Tool/Technology, Soft Skill)
- Each skill has a proficiency level (0-100%)

#### **Projects**
- Add your portfolio projects
- Fields: Title, Description, Short Description, Technologies, GitHub URL, Live URL, Image URL, Date Completed

#### **Certifications**
- Add your professional certifications
- Fields: Title, Issuer, Issue Date, Expiry Date, Credential ID, Credential URL

#### **Education**
- Add your educational background
- Fields: Degree, Institution, Field of Study, Start Date, End Date, GPA, Description

## Sample Data

The system comes pre-populated with sample data about "Ujwal" that matches the resume format. You can:

1. **Keep the sample data** and just update the fields with your information
2. **Delete all data** and start fresh:
   ```bash
   python manage.py populate_portfolio
   # Or manually delete entries from admin panel
   ```

## Key Features

✅ **Dynamic Content**: All portfolio content is stored in the database
✅ **Easy Management**: Use Django Admin to update content
✅ **No Coding Required**: Update your portfolio through the admin interface
✅ **Professional Styling**: Beautiful, responsive design maintained
✅ **Animations**: All animations and smooth transitions work with dynamic data
✅ **Mobile Responsive**: Works perfectly on all devices

## Development Server

To run the development server:
```bash
python manage.py runserver
```

Access at: `http://localhost:8000/`

## Accessing Different Sections

- Homepage: `http://localhost:8000/`
- About: `http://localhost:8000/about/`
- Skills: `http://localhost:8000/skills/`
- Projects: `http://localhost:8000/projects/`
- Experience: `http://localhost:8000/experience/`
- Certifications: `http://localhost:8000/certifications/`
- Resume: `http://localhost:8000/resume/`
- Contact: `http://localhost:8000/contact/`
- Admin Panel: `http://localhost:8000/admin/`

## Customization Tips

### Adding More Information
- You can add more fields to any model by editing `main/models.py` and running:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### Styling
- CSS is located in `static/css/style.css`
- All template styles are preserved and work with the dynamic data

### Adding New Sections
- Create a new model in `models.py`
- Register it in `admin.py`
- Create/update templates to display the data
- Create a view function to fetch and display data

## File Structure

```
Portfolio2/
├── main/
│   ├── migrations/           # Database migrations
│   ├── management/
│   │   └── commands/
│   │       └── populate_portfolio.py  # Sample data loader
│   ├── admin.py              # Admin configuration
│   ├── models.py             # Data models
│   ├── views.py              # View functions
│   └── urls.py               # URL routing
├── portfolio/
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL routing
│   └── wsgi.py               # Production settings
├── templates/
│   └── main/                 # HTML templates
├── static/
│   ├── css/                  # Stylesheets
│   └── js/                   # JavaScript files
└── manage.py                 # Django management script
```

## Database

The project uses SQLite by default (db.sqlite3). This is perfect for development and can be used for production on smaller sites.

For production deployment to multiple users, consider upgrading to:
- PostgreSQL
- MySQL
- Other production databases

## Next Steps

1. ✅ **Update your profile** in the admin panel with your actual information
2. ✅ **Add your experience** - List all your work positions
3. ✅ **Add your skills** - Include all technical and soft skills
4. ✅ **Add your projects** - Showcase your best work
5. ✅ **Add certifications** - Include professional achievements
6. ✅ **Add education** - List your degrees and educational background

## Support

For questions about Django:
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Admin Guide](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

For template modifications:
- HTML templates are in `templates/main/`
- Use Django template tags: `{{ variable }}`, `{% for %} ... {% endfor %}`, etc.

## Production Deployment

When ready to deploy:
1. Set `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Use environment variables for sensitive data
5. Collect static files: `python manage.py collectstatic`
6. Use a production server (Gunicorn, uWSGI, etc.)

---

**Your beautiful portfolio is now powered by dynamic content!** 🚀
