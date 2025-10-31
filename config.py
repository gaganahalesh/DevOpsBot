#!/usr/bin/env python3
"""
🚀 DevOps AI ChatBot - Configuration Settings
Hackathon 2025 - Professional Configuration Management
"""

# AI Model Settings
MODEL_NAME = "all-mpnet-base-v2"
MODEL_DIMENSION = 768
CONFIDENCE_THRESHOLD = 0.6
MAX_SOLUTIONS = 5

# FAISS Search Settings
SEARCH_K = 5  # Number of nearest neighbors to retrieve
INDEX_TYPE = "IndexFlatL2"  # L2 distance for similarity

# Server Settings
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEBUG_MODE = True

# API Settings
API_TITLE = "🚀 DevOps AI ChatBot API - Hackathon 2025"
API_VERSION = "2.0.0"
API_DESCRIPTION = "🤖 Enterprise-grade DevOps Issue Resolution & Pipeline Troubleshooting API powered by Advanced AI + Vector Search"

# File Paths
DATA_FILE = "data/DevOps-Data.xlsx"
MODEL_CACHE_DIR = "models/"
FAISS_INDEX_FILE = "devops_faiss.index"

# Pipeline Integration Settings (for demo purposes - use environment variables in production)
JENKINS_USER = None  # Set to None to use environment variables
JENKINS_PASS = None  # Set to None to use environment variables  
JENKINS_CA_BUNDLE = None  # Set CA bundle path or None to use environment variables


# DevOps Categories (for enhanced analysis)
DEVOPS_CATEGORIES = [
    "Docker",
    "Kubernetes", 
    "Jenkins",
    "GitLab CI/CD",
    "Terraform",
    "Ansible",
    "AWS",
    "Azure",
    "General Infrastructure"
]

# Hackathon Branding
HACKATHON_NAME = "Hackathon 2025"
PROJECT_NAME = "DevOps AI ChatBot"
TEAM_SLOGAN = "🤖 Transforming DevOps with AI"

# Logging Settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Performance Settings
TIMEOUT_SECONDS = 30
MAX_CONCURRENT_REQUESTS = 100
BATCH_SIZE = 10

print("✅ DevOps AI ChatBot Configuration Loaded Successfully!")