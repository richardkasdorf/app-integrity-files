# Integrity hash Service Architecture 


## Overview


## Architecture Layers


### API Layer


### Services Layer


### Repository Layer


### Data Base Layer


### Core Layer


### Test Layer


## Project Structure

projeto_integridade/
│
├── app/
│   ├── main.py                 # FastAPI
│   │
│   ├── api/                    # rotas da API
│   │   ├── __init__.py
│   │   ├── upload_router.py
│   │   └── verify_router.py
│   │
│   ├── services/               # lógica de negócio (coração do sistema)
│   │   ├── __init__.py
│   │   ├── integrity_service.py
│   │   └── hash_service.py
│   │
│   ├── repositories/           # acesso ao banco
│   │   ├── __init__.py
│   │   └── file_repository.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   │
│   └── core/
│       ├── config.py
│       └── utils.py
│
├── tests/
├── data/
├── pytest.ini
└── README.md