# Asset Manager

A web-based asset management system with authentication, laptop tracking, employee management, security items, and report notes.

## Quick Start (Easiest Way)

### Windows Users
**Double-click `start_server.bat`** to start the application automatically.

### PowerShell Users
Run `.\start_server.ps1` in PowerShell.

### Manual Start
```powershell
C:\Users\RITESH\AppData\Local\Programs\Python\Python313\python.exe backend.py
```

## Access the Application

1. Open your web browser
2. Go to: `http://localhost:5000`
3. Login with:
   - Username: `admin`
   - Password: `admin123`

## Features

- **User Authentication**: Login/logout with session management
- **Laptop Management**: Track laptop name, asset ID, employee ID, RAM, ROM, serial number, Bitdefender status, and policy name
- **Employee Management**: Create and edit employee records with ID, email, number, and role
- **Security Items**: Editable security action list
- **Report Notes**: Editable sticky-note style report entries
- **Dark Mode**: Theme toggle stored in the browser

## Setup (Alternative Manual Method)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the backend server:
   ```bash
   python backend.py
   ```

3. Open your browser to `http://localhost:5000`

## Default Credentials

- **Admin**: username: `admin`, password: `admin123`
- Create additional users through the registration form

## API Endpoints

### Authentication
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout
- `GET /auth/me` - Get current user info
- `POST /auth/register` - User registration

### Assets (Authenticated)
- `GET /assets` - Get all assets
- `POST /assets` - Add new asset
- `PUT /assets/<id>` - Update asset
- `DELETE /assets/<id>` - Delete asset

### Users (Admin Only)
- `GET /users` - Get all users
- `POST /users` - Create user
- `PUT /users/<id>` - Update user
- `DELETE /users/<id>` - Delete user

### Security (Authenticated)
- `GET /security` - Get all security items
- `POST /security` - Create security item
- `PUT /security/<id>` - Update security item
- `DELETE /security/<id>` - Delete security item

### Reports (Authenticated)
- `GET /reports` - Get all report notes
- `POST /reports` - Create report note
- `PUT /reports/<id>` - Update report note
- `DELETE /reports/<id>` - Delete report note

## Data Persistence

All data is stored in JSON files:
- `assets.json` - Asset data
- `users.json` - User accounts
- `reports.json` - Report notes
- `security.json` - Security items

## Deploy On Render With Docker

This repo is now configured for Docker-based deployment on Render.

Files added for deployment:
- `Dockerfile`
- `requirements.txt`
- `.dockerignore`
- `render.yaml`

### Option 1: Deploy From `render.yaml`

1. Push this project to GitHub.
2. In Render, choose `New +` -> `Blueprint`.
3. Connect the repo.
4. Render will detect `render.yaml` and create the web service.
5. Deploy.

### Option 2: Deploy As A Docker Web Service

1. Push this project to GitHub.
2. In Render, choose `New +` -> `Web Service`.
3. Select the repo.
4. Render should detect the `Dockerfile`.
5. Add an environment variable named `SECRET_KEY` if you are not using `render.yaml`.
6. Deploy.

### Important Note About Free Render Storage

Render free web services use ephemeral disk storage. That means:
- `assets.json`
- `users.json`
- `reports.json`
- `security.json`

can reset when the service is rebuilt or restarted.

If you want persistent production data, the next step is to move these JSON files to a real database such as PostgreSQL or Render Disk on a paid plan.
