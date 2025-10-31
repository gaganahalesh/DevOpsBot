# DevOps ChatBot Startup Script

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.devops_ai_engine import main as analyze_devops_issue

def display_welcome_banner():
    """Display professional welcome banner for hackathon demo"""
    print("\n" + "🌟" * 60)
    print("🚀" + " " * 20 + "DEVOPS AI CHATBOT - HACKATHON 2025" + " " * 20 + "🚀")
    print("🌟" * 60)
    print("🔥 Intelligent DevOps Issue Resolution & Pipeline Troubleshooting")
    print("⚡ Powered by: Advanced AI + Vector Search + Real-time Analysis")
    print("🎯 Enterprise-Grade: CI/CD Failure Detection & Automated Solutions")
    print("=" * 120)
    print("💡 How to use:")
    print("   • Describe your DevOps issue or pipeline failure")
    print("   • Get AI-powered root cause analysis")
    print("   • Receive step-by-step solution recommendations")
    print("   • Type 'exit' or 'quit' to end session")
    print("=" * 120)

def get_user_input():
    """Get user input with professional prompt"""
    print("\n" + "🔧" * 40)
    print("🤖 DevOps AI Assistant: Ready to analyze your issue...")
    print("🔧" * 40)
    user_input = input("\n💬 Please describe your DevOps issue: ").strip()
    return user_input

def main():
    """Interactive DevOps ChatBot with continuous conversation"""
    display_welcome_banner()
    
    try:
        while True:
            # Get user input
            user_issue = get_user_input()
            
            # Check for exit conditions
            if user_issue.lower() in ['exit', 'quit', 'bye', 'end']:
                print("\n" + "🎉" * 50)
                print("🏆 Thank you for using DevOps AI ChatBot!")
                print("🚀 Your DevOps issues have been successfully analyzed!")
                print("💡 Visit us again for more AI-powered solutions!")
                print("🎉" * 50)
                break
            
            # Check for empty input
            if not user_issue:
                print("⚠️  Please provide a valid DevOps issue description.")
                continue
            
            try:
                print("\n" + "⚡" * 80)
                print("🔍 ANALYZING YOUR DEVOPS ISSUE...")
                print("⚡" * 80)
                
                # Run AI analysis with user input
                analyze_devops_issue(user_issue)
                
                print("\n" + "✅" * 60)
                print("🎯 ANALYSIS COMPLETE! Check the recommendations above.")
                print("✅" * 60)
                
            except Exception as e:
                print(f"\n❌ Error during analysis: {e}")
                print("🔄 Please try rephrasing your issue or contact support.")
        
    except KeyboardInterrupt:
        print("\n\n🛑 Session interrupted by user")
        print("👋 DevOps AI ChatBot session ended")
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()