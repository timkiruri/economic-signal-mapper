#!/usr/bin/env python3
"""
Price Tracking API Startup Script
"""
import uvicorn
import os
from src.database.db import init_db

def main():
    """Main startup function"""
    print("🚀 Starting Price Tracking API...")
    
    # Initialize database
    print("📊 Initializing database...")
    init_db()
    
    # Get configuration from environment
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    reload = os.getenv("RELOAD", "true").lower() == "true"
    
    print(f"🌐 Server will start on http://{host}:{port}")
    print("📝 API documentation available at http://localhost:8000/docs")
    
    # Start the server
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )

if __name__ == "__main__":
    main()