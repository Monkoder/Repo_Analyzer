# 🔍 Repo_Analyzer

> **Automated GitHub Repository System Design, Flaw Detection, and Architecture Synthesis Engine.**

Repo_Analyzer is an intelligent static analysis and architecture synthesis backend built with FastAPI and Python. It ingests GitHub repositories, analyzes dependency manifests and project hierarchies, detects architectural flaws, and synthesizes comprehensive High-Level Design (HLD), Low-Level Design (LLD), and dynamic Mermaid.js C4 diagrams.

---

## 🚀 Key Features

- **⚡ Async GitHub Ingestion**: Recursively navigates Git trees and extracts manifest files without cloning massive codebases.
- **📦 Multi-Ecosystem Dependency Parser**: Identifies frameworks, databases, messaging queues, and caching layers across Node.js, Python, Go, Rust, Java, and Docker.
- **🏗️ Architectural Paradigm Classifier**: Automatically determines architectural styles (Clean Architecture, MVC, Microservices, Modular Monoliths).
- **🛡️ Anti-Pattern & Flaw Detector**: Evaluates systems against 20+ architectural rules to flag Single Points of Failure (SPOFs), missing auth/CORS, synchronous blocking I/O, and missing health checks.
- **📊 Dynamic Diagram Synthesizer**: Generates Mermaid.js syntax for C4 Context/Container/Component diagrams, sequence flows, and ER diagrams.
- **🤖 AI System Design Synthesizer**: Generates rich architectural documentation, trade-off matrices, and interactive Q&A.
- **🔒 Enterprise-Grade Security**: HMAC-SHA256 signature verification, timing-safe equality checks, and replay attack prevention.

---

## 🗂️ Project Structure

```text
backend/
├── app/
│   ├── api/
│   │   └── routes.py              # REST API endpoints & route handlers
│   ├── core/
│   │   ├── config.py              # Pydantic Settings & environment configuration
│   │   └── security.py            # HMAC verification & cryptographic utilities
│   ├── models/
│   │   └── schemas.py             # Pydantic DTOs & response/request schemas
│   ├── services/
│   │   ├── architecture_classifier.py  # Architectural pattern detection
│   │   ├── diagram_generator.py        # Mermaid & C4 diagram generation
│   │   ├── flaw_detector.py            # Anti-pattern & vulnerability rules
│   │   ├── github_ingest.py            # Async Git tree & manifest ingestion
│   │   └── manifest_parser.py          # Package manifest & dependency parsing
│   └── main.py                    # FastAPI application initialization & middleware
├── requirements.txt               # Production & development dependencies
└── run.py                         # ASGI server runner (Uvicorn)
```

---

## 🌐 Supported Tech Ecosystems

| Ecosystem | Manifests / Indicators | Detected Components |
| :--- | :--- | :--- |
| **Node.js / JS / TS** | `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `turbo.json` | Express, NestJS, Next.js, Fastify, Prisma, TypeORM |
| **Python** | `requirements.txt`, `pyproject.toml`, `Pipfile`, `setup.py` | FastAPI, Django, Flask, SQLAlchemy, Celery, PyTorch |
| **Go** | `go.mod`, `go.sum` | Gin, Fiber, Chi, GORM, Echo |
| **Rust** | `Cargo.toml`, `Cargo.lock` | Actix-web, Axum, Tokio, Diesel, SeaORM |
| **Java / JVM** | `pom.xml`, `build.gradle`, `build.gradle.kts` | Spring Boot, Micronaut, Quarkus, Hibernate |
| **Container & Infra** | `Dockerfile`, `docker-compose.yml`, `k8s/*.yaml`, `*.tf` | Postgres, Redis, Kafka, RabbitMQ, Nginx, Kubernetes |

---

## 🗺️ Roadmap & Sprint Milestones

| Sprint | Engine / Module | Status | Description |
| :---: | :--- | :---: | :--- |
| **1** | **FastAPI Core & Swagger UI** | `ACTIVE` | Async ASGI server, CORS, Pydantic v2 schemas, and OpenAPI interactive docs. |
| **2** | **HMAC-SHA256 Security Engine** | `PLANNED` | Cryptographic signature validation, timing-attack prevention, and commit-tree fingerprinting. |
| **3** | **GitHub Ingestion Service** | `PLANNED` | Asynchronous recursive Git tree extraction and selective manifest file download via GitHub REST API. |
| **4** | **Tech Stack Parser** | `PLANNED` | Multi-ecosystem dependency classification across 10 architectural categories. |
| **5** | **Architecture & Paradigm Classifier** | `PLANNED` | Directory pattern analysis identifying Clean Architecture, MVC, Microservices, and Monorepos. |
| **6** | **Route & Schema Extractor** | `PLANNED` | API catalog generator and ORM/SQL entity-relationship schema extractor. |
| **7** | **Flaw & Anti-Pattern Detector** | `PLANNED` | Static heuristic engine flagging SPOFs, blocking I/O, security smells, and DB indexing flaws. |
| **8** | **Actionable Remediation Engine** | `PLANNED` | Before/After code refactoring snippet generator, health score computation, and technical debt index. |
| **9** | **AI System Design Synthesizer** | `PLANNED` | LLM-powered HLD & LLD narrative generator and interactive Q&A. |
| **10** | **Mermaid C4 Diagram Synthesizer** | `PLANNED` | Automatic generation of C4 Context/Container/Component, Sequence, and ER Mermaid diagrams. |

---

## 🛠️ Getting Started

### Prerequisites

- **Python 3.10+**
- **pip** (Python package manager)
- *(Optional)* **Git**

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Monkoder/Repo_Analyzer.git
   cd Repo_Analyzer
   ```

2. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

3. **Create and activate a virtual environment**:
   ```bash
   # On macOS/Linux:
   python -m venv venv
   source venv/bin/activate

   # On Windows (PowerShell):
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Environment Configuration**:
   Create a `.env` file in the `backend/` directory:
   ```env
   PROJECT_NAME="Repo_Analyzer Backend"
   ENVIRONMENT="development"
   DEBUG=True
   HOST="127.0.0.1"
   PORT=8000
   SECRET_KEY="your-super-secret-key-min-32-characters"
   ```

6. **Start the development server**:
   ```bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```
   *Alternatively, run the runner script:*
   ```bash
   python run.py
   ```

---

## 📖 API Documentation & Diagnostics

Once the server is running, explore the interactive OpenAPI documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Core Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Service uptime, semantic version, and runtime diagnostics probe |
| `GET` | `/info` | Capabilities, supported tech ecosystems, and roadmap milestones |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'feat: add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
