# Plataforma de Estudos - Educational Platform

## Overview
This is a Portuguese-language educational platform that provides:
- Interactive quizzes (simulados) on various medical/health topics
- Video lessons (videoaulas)
- Supplementary materials (materiais complementares)
- Admin panel for file management (password-protected)
- A clean, modern interface with purple and dark theme

**Current State**: Fully functional with admin file upload system. Flask backend with SQLite database.

**Last Updated**: November 29, 2025

## Project Architecture

### Technology Stack
- **Backend**: Python 3.11 with Flask
- **Database**: SQLite (database.db)
- **Frontend**: HTML, CSS, JavaScript (Jinja2 templates)
- **Styling**: Custom CSS with purple/dark theme
- **File Storage**: Local uploads folder

### File Structure
```
.
├── app.py                        # Flask application (main backend)
├── database.db                   # SQLite database (file metadata)
├── uploads/                      # Uploaded files storage
├── templates/
│   ├── index.html                # Main landing page with 3 tabs
│   ├── admin.html                # Admin dashboard for file management
│   └── admin_login.html          # Password login page
├── simulado_vigilancia.html      # 50-question quiz (legacy)
├── server.py                     # Legacy static server (not used)
└── replit.md                     # This documentation file
```

### Key Features

#### 1. Landing Page (templates/index.html)
- Three-tab navigation: "Simulados", "Videoaulas", "Materiais Complementares"
- Black and purple theme
- Dynamic file listing from database
- Embedded YouTube video player
- Responsive design

#### 2. Admin Panel (/admin)
- Password-protected access (uses ADMIN_PASSWORD secret)
- File upload with category selection:
  - Simulado: Goes to Simulados tab
  - Aula: Goes to Videoaulas tab
  - Material: Goes to Materiais Complementares tab
- File management (view, delete)
- Title and description for each file

#### 3. Quiz Application (simulado_vigilancia.html)
- 50 multiple-choice questions on PNI, vaccines, epidemiology
- Timer, scoring, explanations

## Environment Variables

### Required Secrets
- `ADMIN_PASSWORD`: Password for admin panel access (REQUIRED)

### Optional
- `SECRET_KEY`: Flask session secret (auto-generated if not set)

## Development Setup

### Running Locally
The Flask server runs on `0.0.0.0:5000` with:
- Debug mode enabled
- Cache headers disabled
- SQLite database auto-initialization

### Database Schema
```sql
CREATE TABLE files (
    id TEXT PRIMARY KEY,
    filename TEXT NOT NULL,
    original_name TEXT NOT NULL,
    category TEXT NOT NULL,      -- 'simulado', 'aula', or 'material'
    title TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Deployment

The project uses autoscale deployment with gunicorn for production.

## User Preferences
None specified yet.

## Recent Changes

### November 29, 2025 - Admin File Upload System
- Added Flask backend with SQLite database
- Created password-protected admin panel
- Implemented file upload with category selection
- Added "Materiais Complementares" tab
- Dynamic file listing from database
- Security improvements (no hardcoded passwords)

### November 29, 2025 - Initial Replit Setup
- Imported from GitHub
- Configured web server workflow on port 5000
- Created project documentation

## Notes
- The admin panel is accessed via the "Admin" button in the top-right corner
- Uploaded files are stored in the `uploads/` folder
- Supported file types: PDF, DOC, DOCX, PPT, PPTX, TXT, MP4, MP3, JPG, JPEG, PNG, GIF, HTML
- The legacy quiz (simulado_vigilancia.html) is served statically
