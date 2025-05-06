# 🚨 Risk Scoring API

A secure, Dockerized REST API for computing mock "risk scores" based on metadata about AI models. Built with **Django** and **Django REST Framework**, this project simulates real-world AI risk assessment logic for compliance and auditing use cases.

---

## 📌 Features

- ✅ RESTful API endpoint: `/api/v1/risk-score`
- 🔐 Token-based authentication (DRF TokenAuth)
- 📊 Rule-based risk logic with capped scoring (0–100)
- 🐳 Dockerized for easy local development and cloud-readiness

---

## 🧰 Tech Stack

- **Python** 3.11  
- **Django** 4.x  
- **Django REST Framework**  
- **Docker** + `docker-compose`

---

## 🚀 Getting Started (Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/pranavkamat7/risk_scoring_api.git
cd risk_scoring_api
cd risk-scoring-api
cd riskapi
```

If you are using windows(my case) then you must do following step:-

---

```
Open entrypoint.sh in VS Code (or any good editor).
Bottom-right → click CRLF → change to LF.
Save the file.
```

### 2. Build and Run the Containers

```bash
docker-compose build
docker-compose up
```

Your API should now be running at: [http://localhost:8000](http://localhost:8000)

---

## 🔑 Authentication

### Create a Superuser and Token

In a separate terminal:

```bash
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py drf_create_token your_username
```

Copy the generated token — you’ll use it to authenticate your API requests.

---

## 🧪 Example: Testing with Postman

**POST** `http://localhost:8000/api/v1/risk-score`

### 🔐 Headers:
```http
Authorization: Token your_token_here
Content-Type: application/json
```

### 📦 JSON Payload:
```json
{
  "purpose": "marketing",
  "data_sensitivity": "high",
  "region": "EU",
  "processor_name": "UnknownVendor"
}
```

### ✅ Sample Response:
```json
{
  "risk_score": 65,
  "risk_breakdown": {
    "region": 30,
    "processor": 20,
    "purpose": 15
  }
}
```

---

## 📈 Scoring Logic

- `region = "EU"` **and** `data_sensitivity = "high"` → +30  
- `processor_name = "UnknownVendor"` → +20  
- `purpose = "marketing"` → +15  
- **Max score**: capped at **100**

---

## 📂 Project Structure

```
risk-scoring-api/risk_scoring_api/riskapi
                                        │
                                        ├── Dockerfile
                                        ├── docker-compose.yml
                                        ├── requirements.txt
                                        ├── riskapi/           # Django project
                                        │   ├── settings.py
                                        │   └── urls.py
                                        ├── scoring/           # Django app
                                        │   ├── models.py
                                        │   ├── views.py
                                        │   └── serializers.py
```

Also without docker you can even run locally by 
```
python manage.py runserver
```
create superuser and create token for it
you can test on postman
