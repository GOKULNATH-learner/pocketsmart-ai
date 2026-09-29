# PocketSmart AI: Your Smart Budget & Recommendation Assistant 🚀

![PocketSmart AI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-8E44AD?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

Managing budgets across different lifestyle needs—like home decor, event planning, or jewelry shopping—can be overwhelming due to the vast variety of products, platforms, and price ranges. **PocketSmart AI** addresses this challenge through a GenAI-powered, cross-platform recommendation system that delivers personalized, budget-based suggestions with direct store query links to **Amazon, Flipkart, IKEA, Pepperfry, Swiggy, Zomato, OYO, and Tanishq**.

---

## 🌟 Key Scenarios & Features

### 1. 🛋️ Home Interior Planning with Smart Budget Allocation
- **Input**: Total budget (₹ INR), room selections (Living Room, Bedroom, Kitchen, Bathroom), interior style preference, and custom item quantities.
- **AI Processing**: Allocates budget across requested rooms and furniture items, recommending cost-effective options from **IKEA, Amazon, Flipkart, and Pepperfry**.

### 2. 🎉 AI-Based Party Budget Planning
- **Input**: Total budget, guest count (pax), event type (Birthday, Wedding, Corporate, Anniversary), and venue style.
- **AI Processing**: Proportionately splits budget across Catering & Food (~45% via **Swiggy & Zomato**), Venue & Stay (~28% via **OYO**), Decoration (~15% via **Amazon**), and Entertainment (~10% via **BookMyShow**).

### 3. 💎 Jewelry Recommendations for Occasions (Multimodal)
- **Input**: Budget, occasion type, jewelry style preference, and **optional outfit image upload**.
- **AI Processing**: Performs multimodal color coordination & aesthetic analysis on uploaded outfit photos using Gemini AI, recommending matching jewelry from **Amazon, Flipkart, Tanishq, and CaratLane**.

### 4. 🔐 Secure Authentication & Recommendation History
- **Security**: Password hashing with `passlib`/`bcrypt`, JWT session management delivered via **HTTP-only cookies**.
- **History Tracking**: Automatically saves budget allocation plans to a persistent SQLite database (`/history`, `/recommendations-details/{id}`).

### 5. ⚡ Smart Fallback Engine
- Features a deterministic AI recommendation fallback engine so the application functions 100% reliably out-of-the-box even if no `GEMINI_API_KEY` is provided or if network limits are reached.

---

## 🏗️ Tech Stack & Architecture

- **Backend**: FastAPI (Python 3.10+) with Uvicorn server.
- **AI Multimodal Layer**: Google GenAI SDK (`google-genai`) configured with `GEMINI_MODEL` (`gemini-2.5-flash`).
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism dark design system), JavaScript, Jinja2 Templates.
- **Database**: SQLite3 for user accounts and recommendation history tracking.
- **Image Processing**: Pillow (`PIL.Image`) for file size validation (5MB max), MIME check, and image resizing.

---

## 📁 File & Project Structure

```
pocketsmart-ai/
├── app/
│   ├── main.py              # FastAPI app initialization, middleware, routes
│   ├── config.py            # Environment & app settings (GEMINI_MODEL, SECRET_KEY)
│   ├── database.py          # SQLite database interface (Users & History)
│   ├── security.py          # Hashing (passlib) & HTTP-Only cookie JWT auth
│   ├── routes/
│   │   ├── auth.py          # Auth routes (/register, /login, /logout, /token)
│   │   ├── home_planner.py  # Home budget planner (/home-planner, /generate-home)
│   │   ├── party_planner.py # Party budget planner (/party-planner, /generate-party)
│   │   ├── jewelry_planner.py# Jewelry budget planner (/jewelry-planner, /generate-jewelry)
│   │   ├── history.py       # Recommendation history (/history)
│   │   └── dashboard.py     # Landing page, dashboard, /health, /startup
│   └── services/
│       └── gemini_utils.py  # Gemini API integration, prompt templates & store link builder
├── static/
│   ├── css/style.css        # Premium glassmorphism dark mode stylesheet
│   └── js/main.js          # Dynamic form interactions & outfit image preview
├── templates/
│   ├── base.html            # Core layout template
│   ├── index.html           # Landing hero page
│   ├── home_planner.html    # Home planner form
│   ├── party_planner.html   # Party planner form
│   ├── jewelry_planner.html # Jewelry planner form with image uploader
│   ├── recommendations.html # AI results presentation with store links
│   ├── history.html         # Saved plans history viewer
│   └── dashboard.html       # User dashboard
├── .env.example             # Environment configuration template
├── .gitignore               # Git ignore setup for Python & secrets
├── Procfile                 # Cloud deployment command for Render / Heroku
├── render.yaml              # Render blueprint deployment file
├── requirements.txt         # Project Python dependencies
├── run.py                   # Server startup script
└── README.md                # Project documentation
```

---

## ⚙️ Installation & Running Locally

### 1. Clone or Download Project
```bash
cd "pocketsmart-ai"
```

### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Setup Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
*(Optional)* Add your Google Gemini API key to `.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
SECRET_KEY=pocketsmart_ai_super_secret_jwt_key_2026
```

### 4. Run Server
```bash
python run.py
```
Open your browser and navigate to **`http://127.0.0.1:8000`**.

---

## 🌐 Deploying to GitHub

To push this codebase to a GitHub repository:

1. **Initialize Git in the project root**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: PocketSmart AI full-stack application"
   ```

2. **Create a new empty repository on GitHub**:
   - Go to [GitHub - Create a New Repository](https://github.com/new).
   - Set repository name: `pocketsmart-ai`.
   - Do **NOT** initialize with README or license (we already have them).

3. **Link remote and push**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/pocketsmart-ai.git
   git push -u origin main
   ```

---

## ☁️ Live Web App Hosting (Render Free Tier)

GitHub hosts project source code. To run the live web application on a public URL for submission/demo:

### Option A: 1-Click Render Deployment using `render.yaml`
1. Go to [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** -> **Blueprints**.
3. Connect your GitHub repository `pocketsmart-ai`.
4. Render will detect `render.yaml` automatically and launch your web service.

### Option B: Manual Web Service Setup on Render
1. Click **New +** -> **Web Service**.
2. Select repository `pocketsmart-ai`.
3. Set Environment to `Python 3`.
4. Set Build Command: `pip install -r requirements.txt`.
5. Set Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
6. Add Environment Variable:
   - `GEMINI_MODEL`: `gemini-2.5-flash`
   - `GEMINI_API_KEY`: *(Your key)*
7. Click **Create Web Service**. Your app will be live at `https://pocketsmart-ai.onrender.com`.

---

## 🧪 Verification & API Health Endpoints

- `GET /health` - Checks application health & Gemini model configuration.
- `GET /startup` - Lists supported planners & store platforms.
- `POST /generate-home` - Home interior budget planner API.
- `POST /generate-party` - Party planner API.
- `POST /generate-jewelry` - Jewelry recommendation API (supports outfit image file upload).

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
