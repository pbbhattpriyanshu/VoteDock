# VoteDock

A modern voting system API built with FastAPI and MongoDB, designed for secure and scalable voting operations.

## Overview

VoteDock is a backend API service that manages voting operations with a clean architecture, async support, and MongoDB integration for data persistence.

## Features

- 🚀 **FastAPI Framework**: High-performance, modern Python web framework
- 🗄️ **MongoDB Integration**: Async database operations with Motor and Beanie ORM
- ✔️ **Data Validation**: Pydantic models for request/response validation
- 🔄 **Async/Await**: Full async support for non-blocking operations
- 📡 **RESTful API**: Clean and intuitive API design
- ⚙️ **Configuration Management**: Environment-based configuration with python-dotenv

## Tech Stack

- **Backend**: FastAPI 0.136.0
- **Server**: Uvicorn 0.44.0
- **Database**: MongoDB with Beanie ORM 2.1.0
- **Async Driver**: Motor 3.7.1
- **Data Validation**: Pydantic 2.13.2
- **Python**: 3.x

## Project Structure

```
VoteDock/
├── Client/                 # Frontend application (coming soon)
├── Server/
│   ├── src/
│   │   ├── main.py        # Application entry point
│   │   ├── api/           # API endpoints
│   │   ├── controllers/   # Business logic
│   │   ├── core/          # Core configurations
│   │   ├── database/      # Database connections
│   │   ├── models/        # Database models
│   │   └── schemas/       # Pydantic schemas
│   ├── requirements.txt   # Project dependencies
│   └── venv/              # Virtual environment
├── README.md              # This file
└── LICENSE                # License file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB instance running (local or cloud)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd VoteDock
   ```

2. **Create and activate virtual environment**
   ```bash
   cd Server
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\Activate.ps1
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the `Server` directory:
   ```env
   MONGODB_URL=mongodb://localhost:27017
   DATABASE_NAME=votedock
   ```

## Running the Application

### Development Server

Run the FastAPI development server with auto-reload:

```bash
cd Server
python -m uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Root Endpoint
- `GET /` - Welcome message and API status

Additional endpoints will be documented as they are implemented.

## Development

### Project Organization

- **API Routes**: Define endpoints in `src/api/`
- **Controllers**: Business logic in `src/controllers/`
- **Models**: Beanie ODM models in `src/models/`
- **Schemas**: Pydantic request/response schemas in `src/schemas/`
- **Database**: MongoDB connection and utilities in `src/database/`

### Adding New Features

1. Create models in `src/models/`
2. Define schemas in `src/schemas/`
3. Implement business logic in `src/controllers/`
4. Add routes in `src/api/`

## License

This project is licensed under the terms in the [LICENSE](LICENSE) file.