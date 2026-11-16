# Online-Gallery for Digital Handicraft
A web application where artists can upload images of their digital handicraft and add detailed descriptions for each piece.

## Features
- Artists can upload images of their work
- Detailed descriptions for each piece
- Gallery view to browse all uploaded works
  
## Tech Stack
| Area | Technology |
|------|------------|
| Backend | Python, Django |
| Database | PostgreSQL |
| Frontend | HTML, CSS, JavaScript |
| Web server | Nginx, Gunicorn |
| HTTPS | Certbot (Let's Encrypt) |
| Hosting | Amazon Web Services (AWS) |

## Getting Started (local setup)
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file (or set environment variables) with your database settings and secret key:

```
SECRET_KEY=your-secret-key
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
```

Then run:

```bash
python manage.py migrate
python manage.py runserver
```

## Deployment
The app runs on an AWS server with Gunicorn serving the Django app behind Nginx, with HTTPS certificates managed by Certbot.

## What I Learned
- Building a full-stack web app with Django and PostgreSQL
- Setting up cloud infrastructure and deploying on AWS
- Configuring Nginx and Gunicorn as a production stack
- Securing a site with HTTPS using Certbot
