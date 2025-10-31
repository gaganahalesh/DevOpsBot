#!/usr/bin/env python3
"""
🚀 DevOps AI ChatBot - Setup & Initialization Script
Hackathon 2025 - One-Click Setup for Professional Demo
"""

import os
import sys
import subprocess
import importlib.util

def print_banner():
    """Display professional setup banner"""
    print("\n" + "="*80)
    print("🚀 DEVOPS AI CHATBOT - HACKATHON 2025 SETUP")
    print("🤖 Enterprise-Grade Pipeline Troubleshooting & Issue Resolution")
    print("="*80)
    print("⚡ Automated setup for professional hackathon demonstration")
    print("📦 Installing dependencies and AI models...")
    print("="*80)

def check_python_version():
    """Ensure Python 3.8+ is available"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Python 3.8+ required")
        print(f"   Current version: {version.major}.{version.minor}")
        print("   Please upgrade Python and try again")
        sys.exit(1)
    else:
        print(f"✅ Python {version.major}.{version.minor} detected - Compatible!")

def install_requirements():
    """Install Python dependencies"""
    print("\n📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        print("💡 Try running: pip install -r requirements.txt manually")
        return False
    return True

def check_required_packages():
    """Verify critical packages are installed"""
    required_packages = [
        "fastapi",
        "uvicorn", 
        "sentence_transformers",
        "faiss",
        "pandas",
        "torch"
    ]
    
    print("\n🔍 Verifying package installation...")
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == "faiss":
                # FAISS might be installed as faiss-cpu
                try:
                    importlib.import_module("faiss")
                except ImportError:
                    importlib.import_module("faiss_cpu")
            else:
                importlib.import_module(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        return False
    else:
        print("✅ All required packages verified!")
        return True

def download_ai_model():
    """Download and cache the AI model"""
    print("\n🤖 Initializing AI models...")
    try:
        # Import sentence transformers to trigger model download
        from sentence_transformers import SentenceTransformer
        
        print("   📥 Downloading sentence-transformers model (all-mpnet-base-v2)...")
        print("   ⏱️  This may take 2-3 minutes on first run...")
        
        # This will download the model if not already cached
        model = SentenceTransformer('all-mpnet-base-v2')
        print("   ✅ AI model ready!")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error downloading AI model: {e}")
        print("   💡 Model will be downloaded automatically on first use")
        return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating project directories...")
    directories = ["models", "data", "logs"]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"   ✅ Created: {directory}/")
        except Exception as e:
            print(f"   ❌ Error creating {directory}/: {e}")

def setup_database():
    """Setup SQLite database from MySQL dump"""
    print("\n🗄️ Setting up DevOps knowledge database...")
    try:
        # Import and run the database converter
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        # Check if scripts directory exists
        if not os.path.exists('scripts'):
            print("⚠️  Scripts directory not found - database setup skipped")
            return True
            
        # Import the converter
        from scripts.convert_to_sqlite import create_sqlite_database
        
        # Create database
        db_path = create_sqlite_database()
        
        # Quick validation - check if database was created
        if os.path.exists('data/devops_issues.db'):
            print("✅ Database setup completed successfully!")
            
            # Quick validation - count records
            try:
                import sqlite3
                conn = sqlite3.connect('data/devops_issues.db')
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM devops_issues")
                count = cursor.fetchone()[0]
                conn.close()
                print(f"📊 Loaded {count} DevOps scenarios for AI analysis")
            except:
                pass
                
            return True
        else:
            print("❌ Database setup failed - will use built-in knowledge base")
            return True
            
    except ImportError:
        print("⚠️  Database setup skipped - will use built-in knowledge base")
        return True
    except Exception as e:
        print(f"❌ Database setup error: {e}")
        print("⚠️  Will use built-in knowledge base as fallback")
        return True

def test_core_functionality():
    """Test core AI engine functionality"""
    print("\n🧪 Testing core functionality...")
    try:
        # Import and test the core engine
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from core.devops_ai_engine import test_ai_engine
        
        if test_ai_engine():
            print("✅ Core AI engine test passed!")
            return True
        else:
            print("❌ Core AI engine test failed")
            return False
            
    except ImportError:
        print("⚠️  Core engine test skipped - will initialize on first use")
        return True
    except Exception as e:
        print(f"❌ Core engine test error: {e}")
        return False

def display_launch_instructions():
    """Show how to launch the application"""
    print("\n" + "="*80)
    print("🎉 SETUP COMPLETE - READY FOR HACKATHON!")
    print("="*80)
    print("🚀 Launch Options:")
    print("")
    print("   🖥️  Interactive CLI:")
    print("      python cli.py")
    print("")
    print("   🌍 Web Interface:")
    print("      python app.py")
    print("      Then open: http://127.0.0.1:8000/chat")
    print("")
    print("   📚 API Documentation:")  
    print("      python app.py")
    print("      Then open: http://127.0.0.1:8000/docs")
    print("")
    print("="*80)
    print("💡 Example DevOps Issues to Try:")
    print("   • 'Docker build failed with permission denied'")
    print("   • 'Jenkins pipeline timeout during deployment'") 
    print("   • 'Kubernetes pod crashloopbackoff error'")
    print("   • 'Terraform apply failed - resource already exists'")
    print("="*80)
    print("🏆 Good luck with your hackathon presentation!")
    print("")

def main():
    """Main setup orchestration"""
    try:
        # Display banner
        print_banner()
        
        # Check Python version
        check_python_version()
        
        # Install requirements
        if not install_requirements():
            print("❌ Setup failed at dependency installation")
            sys.exit(1)
        
        # Verify packages
        if not check_required_packages():
            print("❌ Setup failed at package verification") 
            sys.exit(1)
        
        # Create directories
        create_directories()
        
        # Setup database
        setup_database()
        
        # # Download AI model (optional - will happen on first use anyway)
        # download_ai_model()
        
        # Test functionality
        test_core_functionality()
        
        # Show launch instructions
        display_launch_instructions()
        
    except KeyboardInterrupt:
        print("\n❌ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()