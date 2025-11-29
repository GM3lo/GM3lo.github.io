# Plataforma de Estudos - Educational Platform

## Overview
This is a Portuguese-language educational platform that provides:
- Interactive quizzes (simulados) on various medical/health topics
- Video lessons (videoaulas) 
- A clean, modern interface with purple and dark theme

**Current State**: Fully functional and ready to use. The platform is a static website serving HTML pages with embedded JavaScript for quiz functionality.

**Last Updated**: November 29, 2025

## Project Architecture

### Technology Stack
- **Frontend**: Pure HTML, CSS, JavaScript
- **Styling**: Tailwind CSS (loaded via CDN)
- **Server**: Python 3.11 HTTP server (development)
- **Deployment**: Static site hosting

### File Structure
```
.
├── index.html                    # Main landing page (navigation hub)
├── simulado_vigilancia.html      # 50-question quiz on viral infections and PNI
├── server.py                     # Development HTTP server
└── replit.md                     # This documentation file
```

### Key Features

#### 1. Landing Page (index.html)
- Two-tab navigation: "Simulados" and "Videoaulas"
- Black and purple theme
- Links to available quizzes
- Embedded YouTube video player
- Responsive design

#### 2. Quiz Application (simulado_vigilancia.html)
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

## Development Setup

### Running Locally
The project uses a Python HTTP server configured to:
- Serve on `0.0.0.0:5000`
- Disable caching (for development)
- Serve static HTML files

The workflow "Web Server" automatically starts the server when the project loads.

### Deployment
The project is configured for static deployment, serving files from the current directory. The static deployment configuration means the HTML files are served directly without needing the Python server in production.

## User Preferences
None specified yet.

## Recent Changes

### November 29, 2025 - Initial Replit Setup
- Renamed `README.md` to `index.html` for proper web serving
- Created `server.py` for local development
- Configured web server workflow on port 5000
- Set up static deployment configuration
- Added cache-control headers to prevent stale content
- Created project documentation

## Notes
- The quiz data is embedded directly in the HTML file (simulado_vigilancia.html)
- All styling is inline or via CDN (Tailwind CSS)
- No build process required
- No external dependencies beyond the Tailwind CSS CDN
- The platform is fully client-side (no backend API)
