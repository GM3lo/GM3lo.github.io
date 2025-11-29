# Plataforma de Estudos - Educational Platform

## Overview
This is a Portuguese-language educational platform that provides:
- Interactive quizzes (simulados) on various medical/health topics
- Video lessons (videoaulas) 
- Supplementary materials (materiais complementares)
- Admin panel for adding resources dynamically
- A clean, modern interface with purple and dark theme

**Current State**: Fully functional with admin panel. The platform is a static website serving HTML pages with embedded JavaScript for quiz functionality and dynamic resource management.

**Last Updated**: November 29, 2025

## Project Architecture

### Technology Stack
- **Frontend**: Pure HTML, CSS, JavaScript
- **Styling**: Tailwind CSS (loaded via CDN)
- **Server**: Python 3.11 HTTP server (development)
- **Storage**: Browser localStorage (client-side)
- **Authentication**: Simple password-based (localStorage)
- **Deployment**: Static site hosting

### File Structure
```
.
├── index.html                    # Main landing page with 3 tabs (Simulados, Videoaulas, Materiais)
├── admin.html                    # Admin panel for managing resources
├── simulado_vigilancia.html      # 50-question quiz on viral infections and PNI
├── server.py                     # Development HTTP server
└── replit.md                     # This documentation file
```

### Key Features

#### 1. Landing Page (index.html)
- Three-tab navigation: "Simulados", "Videoaulas", and "Materiais Complementares"
- Black and purple theme
- Links to available quizzes and resources
- Embedded YouTube video player
- Responsive design
- Dynamic loading of admin-created resources
- Admin icon (⚙️) in the header for quick access to admin panel

#### 2. Admin Panel (admin.html)
- **Login**: Password-protected (default password: `admin123`)
- **Add Resources**: Upload/add new resources with:
  - Title
  - URL/Link
  - Category (Simulados, Videoaulas, or Materiais Complementares)
  - Optional description
- **List Resources**: View all created resources
- **Delete Resources**: Remove resources from the platform
- **Data Storage**: Resources stored in browser localStorage (persistent)

#### 3. Quiz Application (simulado_vigilancia.html)
- 50 multiple-choice questions on:
  - Brazilian National Immunization Program (PNI)
  - Viral infections
  - Vaccines
  - Epidemiological surveillance
- Features:
  - Timer tracking elapsed time
  - Interactive question answering
  - Automatic scoring
  - Detailed explanations for each answer
  - Visual feedback (correct/wrong answers)

## How to Use the Admin Panel

1. **Access Admin**: Click the ⚙️ icon in the top-right of the main page, or go to `/admin.html`
2. **Login**: Enter the admin password (default: `admin123`)
3. **Add Resources**:
   - Fill in the resource title
   - Enter the URL/link to the resource
   - Select the category (which section it will appear in)
   - Optionally add a description
   - Click "Adicionar Recurso" (Add Resource)
4. **View Resources**: Click on the "Listar Recursos" tab to see all created resources
5. **Delete Resources**: Click the delete button next to any resource

## How Resources Appear

- **Simulados**: New resources appear as links below the main quiz
- **Videoaulas**: New resources appear as links below the YouTube video
- **Materiais Complementares**: New resources fill the entire section

## Development Setup

### Running Locally
The project uses a Python HTTP server configured to:
- Serve on `0.0.0.0:5000`
- Disable caching (for development)
- Serve static HTML files

The workflow "Web Server" automatically starts the server when the project loads.

### Deployment
The project is configured for static deployment. In production, resources persist in localStorage on each user's browser (or can be migrated to a backend database if needed).

## User Preferences
None specified yet.

## Recent Changes

### November 29, 2025 - Admin Panel Implementation
- Created `/admin.html` with login and resource management
- Modified `/index.html` to:
  - Add admin panel icon in header
  - Add "Materiais Complementares" tab
  - Implement dynamic resource loading from localStorage
  - Auto-refresh resources when returning from admin panel
- Resources now managed entirely through admin panel
- All data persisted in localStorage

### November 29, 2025 - Initial Replit Setup
- Renamed `README.md` to `index.html` for proper web serving
- Created `server.py` for local development
- Configured web server workflow on port 5000
- Set up static deployment configuration
- Added cache-control headers to prevent stale content

## Notes
- The quiz data is embedded directly in the HTML file (simulado_vigilancia.html)
- All styling is inline or via CDN (Tailwind CSS)
- No build process required
- No external dependencies beyond the Tailwind CSS CDN
- The platform is fully client-side (no backend API required)
- Admin resources are stored in localStorage (browser storage)
- To change the admin password, modify `DEFAULT_PASSWORD` in admin.html

## Security Notes
- Current implementation uses localStorage and a simple password
- For production with multiple users, migrate to a proper backend (Node.js/Express, Python/Flask, etc.)
- Consider using proper authentication (OAuth, JWT, etc.) if expanding to multiple admin users
