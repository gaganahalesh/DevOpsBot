#!/usr/bin/env python3
"""
🚀 DevOps AI ChatBot - FastAPI Web Interface
Professional web interface for enterprise DevOps troubleshooting
Hackathon 2025 - AI-Powered Solution Recommendations
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import sys
import os
from typing import Optional

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Pydantic models for request/response
class DevOpsQuery(BaseModel):
    issue: str
    include_confidence: Optional[bool] = True
    max_solutions: Optional[int] = 5

class DevOpsSolution(BaseModel):
    failure: str
    root_cause: str
    solution: str
    confidence: float
    reason: str
    global_index: Optional[int] = None

class DevOpsResponse(BaseModel):
    status: str
    message: str
    query: str
    solutions: list[DevOpsSolution]
    total_solutions: int
    analysis_method: str

# Create the FastAPI app
app = FastAPI(
    title="🚀 DevOps AI ChatBot API - Hackathon 2025",
    description="🤖 Enterprise-grade DevOps Issue Resolution & Pipeline Troubleshooting API powered by Advanced AI + Vector Search",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {
        "message": "🚀 DevOps AI ChatBot - Hackathon 2025", 
        "status": "✅ Server Running",
        "endpoints": {
            "chat": "/chat",
            "analyze": "/devops/analyze", 
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health():
    return {
        "status": "✅ healthy", 
        "server": "🤖 DevOps AI ChatBot",
        "version": "2.0.0",
        "hackathon": "2025"
    }

@app.get("/chat", response_class=HTMLResponse)
async def devops_chat_interface(request: Request):
    """
    🎨 Serve the DevOps AI ChatBot web interface - Clean hackathon version
    """
    return templates.TemplateResponse("chat_interface.html", {"request": request})

@app.post("/devops/analyze", response_model=DevOpsResponse)
async def analyze_devops_issue(query: DevOpsQuery):
    """
    🤖 Analyze DevOps issues with AI-powered solution recommendations
    """
    try:
        print(f"\n🚀 API Request: Analyzing DevOps issue...")
        print(f"📋 User Query: {query.issue[:100]}...")
        
        # Import and run DevOps analysis
        from core.devops_ai_engine import main as run_devops_analysis
        
        # Capture the analysis results
        solutions = run_devops_analysis(query.issue)
        
        # Process solutions for API response
        if solutions and isinstance(solutions, list):
            # Filter by confidence if requested
            if query.include_confidence:
                solutions = [sol for sol in solutions if sol.get('confidence', 0) > 0.6]
            
            # Limit solutions count
            solutions = solutions[:query.max_solutions]
            
            # Convert to Pydantic models
            solution_models = []
            for sol in solutions:
                solution_models.append(DevOpsSolution(
                    failure=sol.get('Failure', 'N/A'),
                    root_cause=sol.get('Root Cause', 'N/A'),
                    solution=sol.get('Solution', 'N/A'),
                    confidence=sol.get('confidence', 0.0),
                    reason=sol.get('reason', 'AI analysis'),
                    global_index=sol.get('global_index', 0)
                ))
            
            print(f"✅ Analysis Complete: {len(solution_models)} solutions found")
            
            return DevOpsResponse(
                status="success",
                message=f"Found {len(solution_models)} AI-powered solutions for your DevOps issue",
                query=query.issue,
                solutions=solution_models,
                total_solutions=len(solution_models),
                analysis_method="AI + Vector Search + Confidence Scoring"
            )
        else:
            return DevOpsResponse(
                status="success",
                message="No specific solutions found, but analysis completed",
                query=query.issue,
                solutions=[],
                total_solutions=0,
                analysis_method="AI + Vector Search + Confidence Scoring"
            )
        
    except Exception as e:
        print(f"❌ Error in DevOps analysis: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"DevOps analysis failed: {str(e)}"
        )

@app.get("/devops/analyze")
async def analyze_devops_issue_simple(issue: str):
    """
    🚀 Quick DevOps analysis via GET request (for easy browser testing)
    """
    try:
        print(f"\n🔍 Quick Analysis: {issue[:50]}...")
        
        # Create query object
        query = DevOpsQuery(issue=issue)
        
        # Call the main POST endpoint
        result = await analyze_devops_issue(query)
        
        return {
            "status": result.status,
            "message": result.message,
            "query": result.query,
            "solutions_count": result.total_solutions,
            "solutions": [
                {
                    "failure": sol.failure,
                    "solution": sol.solution,
                    "confidence": f"{sol.confidence:.1%}"
                } for sol in result.solutions
            ],
            "note": "Use POST /devops/analyze for full structured response"
        }
        
    except Exception as e:
        print(f"❌ Error in quick analysis: {e}")
        return {
            "status": "error",
            "message": f"DevOps analysis failed: {str(e)}",
            "query": issue
        }



if __name__ == '__main__':
    print("🚀 Starting DevOps AI ChatBot FastAPI Server...")
    print("📍 Access the web interface at: http://127.0.0.1:8000/chat")
    print("📍 API documentation at: http://127.0.0.1:8000/docs")
    
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )