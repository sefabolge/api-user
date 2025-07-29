# User api

This FastAPI backend fetches and reformats user data from [Reqres.in](https://reqres.in) and exposes it via a clean REST API.

## Getting Started

### 1. Clone project folder
```
git clone https://github.com/sefabolge/api-user.git
```
### 2. Create `.env` file:

```
copy .env-example .env
cp .env-example .env
```
### 3.  Create and activate a venv and instal dependencies
```
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run backend locally
uvicorn app.main:app --reload

```

## Docker Usage

### Build image and run:

```bash
docker build -t lineup-backend .
```
```bash
docker run -p 8000:8000 --env-file .env lineup-backend
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Sample API

```
GET /api/v1/user/2
```

Response:
```
{
  "data": {
    "id": 2,
    "first_name": "Janet",
    "last_name": "Weaver",
    "email": "janet.weaver@reqres.in",
    "avatar": "https://reqres.in/img/faces/2-image.jpg"
  },
  "support": {
    "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
    "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
  }
}
```
---

## Run Tests

```bash
pytest
```

###  Frontend – React + TypeScript (User Info Viewer)
This is a React app that fetches and displays user data from the FastAPI backend.
- User data is fetched from `/api/v1/user/:id

## Getting Started

# 1. Create `.env` file:
```
copy .env-example .env
cp .env-example .env
```
# 2. Install dependencies

```
npm install
npm run dev
```

### Folder Descriptions if need for future

- `utils/`: Shared utility functions (e.g., formatters, helpers).
- `styles/`: Global CSS, theme configuration, and design tokens.
- `components/`: Reusable UI components shared across features.
