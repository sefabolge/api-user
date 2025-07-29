# User api

This FastAPI backend fetches and reformats user data from [Reqres.in](https://reqres.in) and exposes it via a clean REST API.

## Setup

### 1. Clone and enter project folder:

### 2. Create `.env` file:

```env
REQRES_API_KEY=reqres-free-v1
REQRES_API_URL=https://reqres.in/api/users
ALLOWED_ORIGINS=http://localhost:5173
```

## Docker Usage

### Build image:

```bash
docker build -t lineup-backend .
```

### Run container:

```bash
docker run -p 8000:8000 --env-file .env lineup-backend
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Sample API

```
GET /api/v1/user/2
```

Returns formatted user data from Reqres API.

---

## Run Tests

```bash
pytest
```

---

### Folder Descriptions

- `utils/`: Shared utility functions (e.g., formatters, helpers).
- `styles/`: Global CSS, theme configuration, and design tokens.
- `components/`: Reusable UI components shared across features.
