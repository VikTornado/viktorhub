# ViktorHub - Full-Stack Personal Portfolio & Blog

A production-grade full-stack web application built with **Django**, **Next.js**, and **PostgreSQL**. Features a complete CMS for managing projects, blog posts, and notes with multilingual support (EN/UKR).

## 🚀 Tech Stack

### Frontend
- **Next.js 16** (App Router) with JavaScript
- **Tailwind CSS 4** for styling
- **Framer Motion** for animations
- **Axios** for API communication
- **i18n** support (EN/UKR)

### Backend
- **Django 6** + Django REST Framework
- **PostgreSQL** database
- **JWT Authentication** (SimpleJWT)
- **Cloudinary** for media storage (optional)
- **Django Admin** for content management

### DevOps
- **Docker Compose** for containerized development
- **Gunicorn** for production server

## ✨ Features

- 📱 **Fully Responsive** - Works on all devices
- 🌐 **Multilingual** - EN/UKR content with language toggle
- 🎨 **Animated UI** - Smooth transitions with Framer Motion
- 🔐 **JWT Authentication** - Secure API endpoints
- 📝 **Rich Content Editor** - Django Prose Editor for blog posts
- 🖼️ **Image Management** - Cloudinary integration
- 🏷️ **Tag System** - Shared tags across projects and posts
- 🔍 **Search & Filter** - Full-text search and tag filtering
- 📄 **Pagination** - Optimized data loading
- 🐳 **Docker Ready** - One command to run entire stack

## 📋 Prerequisites

- **Docker** and **Docker Compose** (recommended)
- **Node.js** 18+ and **npm** (if running without Docker)
- **Python** 3.10+ (if running without Docker)
- **PostgreSQL** 15+ (if running without Docker)

## 🚀 Quick Start with Docker

### 1. Clone the repository

```bash
git clone https://github.com/VikTornado/viktorhub.git
cd viktorhub
```

### 2. Set up environment variables

**Backend:**
```bash
cd backend
cp .env.example .env
# Edit .env and update values as needed
```

**Frontend:**
```bash
cd frontend
cp .env.example .env
# Usually no changes needed for local development
```

### 3. Start the application

```bash
# From project root
docker compose up --build
```

This will start:
- **PostgreSQL** on port 5432
- **Django backend** on http://localhost:8000
- **Next.js frontend** on http://localhost:3000

### 4. Run migrations and create superuser

In a new terminal:

```bash
# Run migrations
docker compose exec backend python manage.py migrate

# Create admin superuser
docker compose exec backend python manage.py createsuperuser

# Load seed data (optional)
docker compose exec backend python manage.py seed_data
```

### 5. Access the application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api
- **Django Admin**: http://localhost:8000/admin

## 🛠️ Manual Setup (Without Docker)

### Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up .env file
cp .env.example .env
# Configure DATABASE_URL for PostgreSQL or leave blank for SQLite

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load seed data
python manage.py seed_data

# Run development server
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Set up .env file
cp .env.example .env

# Run development server
npm run dev
```

## 📦 Database Seed Data

The `seed_data` management command populates the database with:
- **6 projects** - Full featured projects with descriptions and tech stacks
- **5 blog posts** - Published articles with tags
- **8 notes** - Quick coding tips and snippets
- **15 tags** - Shared across all content types

All content is bilingual (EN/UKR).

```bash
python manage.py seed_data
```

## 🔐 Environment Variables

### Backend (.env)

```env
DEBUG=True
SECRET_KEY=your-secret-key-change-in-production
DATABASE_URL=postgresql://postgres:postgres@db:5432/vikhub
ALLOWED_HOSTS=localhost,127.0.0.1,backend
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
CSRF_TRUSTED_ORIGINS=http://localhost:3000

# Optional: Cloudinary for media storage
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### Frontend (.env)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🎯 API Endpoints

### Public Endpoints (Read-Only)
- `GET /api/projects/` - List all projects
- `GET /api/projects/:slug/` - Get project details
- `GET /api/posts/` - List published blog posts
- `GET /api/posts/:slug/` - Get post details
- `GET /api/notes/` - List all notes
- `GET /api/tags/` - List all tags
- `POST /api/contact/` - Submit contact form

### Protected Endpoints (JWT Required)
- `POST /api/projects/` - Create project
- `PUT /api/projects/:slug/` - Update project
- `DELETE /api/projects/:slug/` - Delete project
- Similar CRUD endpoints for posts, notes, and tags

### Authentication
- `POST /api/token/` - Get JWT tokens
- `POST /api/token/refresh/` - Refresh access token

## 🐙 Git Workflow

### Auto-Push Script

The project includes a convenient auto-push command:

```bash
cd frontend
npm run push
```

Or with a custom commit message:

```bash
MSG="feat: add new feature" npm run push
```

This will:
1. Add all changes (`git add -A`)
2. Commit with the message (`git commit -m "..."`)
3. Push to main branch (`git push -u origin main`)

### First-Time Git Setup

If starting fresh:

```bash
git init
git remote add origin https://github.com/VikTornado/viktorhub.git
git branch -M main
git add -A
git commit -m "Initial commit"
git push -u origin main
```

**Note**: You'll need GitHub authentication (personal access token or SSH key).

## 📱 Frontend Features

### Responsive Navigation
- **Desktop**: Animated header with hover underlines
- **Mobile**: Slide-over menu with full-screen overlay
- **Language Toggle**: EN/UKR switcher (persists in localStorage)

### Max-Width Container
All pages respect a `max-w-[1220px]` constraint via the `.container-custom` class:

```css
.container-custom {
  max-width: 1220px;
  margin: 0 auto;
  padding: 0 1rem;
}
```

### Page Routes
- `/` - Home page with hero and featured projects
- `/projects` - Projects grid with filter/search
- `/projects/[slug]` - Project details page
- `/blog` - Blog posts with search and tags
- `/blog/[slug]` - Blog post details
- `/notes` - Quick notes and tips
- `/about` - About page
- `/contact` - Contact form

## 🔧 Development

### Backend
```bash
cd backend
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm run dev
```

### Build for Production
```bash
cd frontend
npm run build
npm start
```

## 🧪 Testing

### Backend Tests (when implemented)
```bash
cd backend
python manage.py test
```

### Frontend Build Test
```bash
cd frontend
npm run build
```

## 📚 Content Management

Use Django Admin to manage all content:

1. Navigate to http://localhost:8000/admin
2. Log in with superuser credentials
3. Manage:
   - **Projects** - Add cover images, tech stack, repo/live URLs
   - **Blog Posts** - Write with rich text editor, set status (draft/published)
   - **Notes** - Quick snippets and tips
   - **Tags** - Create and assign tags
   - **Contact Messages** - View submissions

## 🚢 Deployment

### Database Migrations on Deploy

Always run migrations after deploying:

```bash
python manage.py migrate
```

### Static Files Collection

```bash
python manage.py collectstatic --noinput
```

### Production Checklist

- [ ] Set `DEBUG=False` in backend `.env`
- [ ] Change `SECRET_KEY` to a strong random value
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Update `CORS_ALLOWED_ORIGINS` with your frontend URL
- [ ] Set up Cloudinary for media storage
- [ ] Configure PostgreSQL database
- [ ] Set up SSL/HTTPS
- [ ] Configure Gunicorn or uwsgi
- [ ] Set up Nginx reverse proxy
- [ ] Enable CSRF protection

## 🐛 Troubleshooting

### Docker Issues

**Services won't start:**
```bash
docker compose down -v
docker compose up --build
```

**Database connection errors:**
- Ensure PostgreSQL service is healthy
- Check `DATABASE_URL` in backend `.env`

### Frontend Issues

**API calls failing:**
- Verify `NEXT_PUBLIC_API_URL` in frontend `.env`
- Check CORS settings in backend

**Build errors:**
```bash
rm -rf .next node_modules
npm install
npm run build
```

### Backend Issues

**ModuleNotFoundError:**
```bash
pip install -r requirements.txt
```

**Migration errors:**
```bash
python manage.py makemigrations
python manage.py migrate
```

## 📄 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👤 Author

**Viktor Minin**
- GitHub: [@VikTornado](https://github.com/VikTornado)
- Project Repo: [viktorhub](https://github.com/VikTornado/viktorhub)

---

Made with ❤️ using Django, Next.js, and Docker
