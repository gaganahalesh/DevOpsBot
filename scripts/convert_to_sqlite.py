#!/usr/bin/env python3
"""
🗄️ MySQL to SQLite Converter for DevOps ChatBot
Convert the MySQL dump to SQLite for standalone hackathon deployment
"""

import sqlite3
import os

def create_sqlite_database():
    """Create SQLite database from the MySQL dump data"""
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Database file path
    db_path = 'data/devops_issues.db'
    
    # Remove existing database
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"🗑️ Removed existing database: {db_path}")
    
    # Create new SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table structure
    cursor.execute('''
        CREATE TABLE devops_issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            failure TEXT NOT NULL,
            root_cause TEXT NOT NULL,
            solution TEXT NOT NULL
        )
    ''')
    
    # Insert data from MySQL dump
    issues_data = [
        (1, "ERROR :: Command(git am <path>/6715314649237516733_patch/*.patch --keep-cr --3way) failed after maximum retry ... script returned exit code 255", 
         "Git patch application failure due to merge conflicts or corrupted patches. The git am command with 3-way merge strategy exhausted retry attempts.", 
         "If there are merge conflicts during git am --3way, rebase your workspace, resolve conflicts if any. Afterwards push the changes and retrigger."),
         
        (2, "Unable to find image 'docker.io/library/hello-world:latest' locally\ndocker: Error response from daemon: pull access denied for hello-world, repository does not exist or may require 'docker login'.", 
         "This error occurs because Docker couldn't pull the image from the private registry due to network timeout, connectivity issues, missing permissions, or an invalid image/tag.", 
         "First check manual docker pull from artifactory. If manual pull also fails, check for the same image and tag in artifactory to verify if it exists."),
         
        (3, "{'Commit issue (Dev)': 'Dynamic Code Coverage Threshold(70%) not met', 'Environment issue': []} INFO :: Environment variables :: {'FAIL_CATEGORY': 'Commit issue (Dev)', 'FAIL_REASON': 'Dynamic Code Coverage Threshold(70%) not met'} script returned exit code 1", 
         "Dynamic Code Coverage Threshold(70%) not is met and minimum requirement set for dynamic code coverage is 70 percent.", 
         "Kindly maintain the minimum coverage and write necessary testcase to increase the coverage."),
         
        (4, "Failure: Stage failed due to error: hudson.AbortException: script returned exit code 1", 
         "This error indicates that script or command within your pipeline stage executed and failed. Jenkins throws this exception when a build step fails. It's Jenkins' way of saying \"something went wrong and we're stopping the build\"", 
         "Examine the console logs. The key is to look at the console output right before this error to see what specific command or script actually failed!"),
         
        (5, "Branch not set issue in pool git status HEAD detached from FETCH_HEAD Untracked files: nothing added to commit but untracked files present (use \"git add\" to track)", 
         "Head detached from master.", 
         "checkout to your branch <your_branch> and then retrigger pool mt."),
         
        (6, "Jenkins Build Timeout", 
         "Jenkins build timing out during execution phase", 
         "1. Increase build timeout 2. Optimize build steps 3. Check system resources"),
         
        (7, "Kubernetes Pod CrashLoopBackOff", 
         "Pod continuously crashes and restarts in Kubernetes cluster", 
         "1. Check pod logs kubectl logs pod-name 2. Verify resource limits 3. Check probes"),
         
        (8, "Jenkins Build Timeout", 
         "Jenkins build timing out during execution phase", 
         "1. Increase build timeout 2. Optimize build steps 3. Check system resources"),
         
        (9, "GitLab CI Pipeline Failure - Dependency Issues", 
         "Pipeline fails due to missing or incompatible dependencies", 
         "1. Update dependency versions 2. Clear pipeline cache 3. Check lock files"),
         
        (10, "Deployment Rollback Required", 
          "Production deployment causing issues requiring immediate rollback", 
          "1. Identify failed deployment 2. Execute rollback 3. Verify service health")
    ]
    
    # Insert all data
    cursor.executemany('''
        INSERT INTO devops_issues (id, failure, root_cause, solution) 
        VALUES (?, ?, ?, ?)
    ''', issues_data)
    
    # Commit and close
    conn.commit()
    
    # Verify insertion
    cursor.execute("SELECT COUNT(*) FROM devops_issues")
    count = cursor.fetchone()[0]
    
    conn.close()
    
    print(f"✅ SQLite database created successfully!")
    print(f"📊 Database: {db_path}")
    print(f"📋 Records inserted: {count}")
    
    return db_path

def load_issues_from_database():
    """Load issues from SQLite database for AI engine"""
    try:
        conn = sqlite3.connect('data/devops_issues.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT failure, root_cause, solution FROM devops_issues")
        rows = cursor.fetchall()
        
        issues = []
        for row in rows:
            issues.append({
                'Failure': row[0],
                'Root Cause': row[1], 
                'Solution': row[2]
            })
        
        conn.close()
        print(f"✅ Loaded {len(issues)} issues from database")
        return issues
        
    except Exception as e:
        print(f"❌ Error loading from database: {e}")
        return []

if __name__ == "__main__":
    print("🚀 Converting MySQL dump to SQLite for hackathon...")
    print("="*60)
    
    # Create database
    db_path = create_sqlite_database()
    
    # Quick validation - check file exists and has content
    if os.path.exists('data/devops_issues.db'):
        print("\n✅ Database conversion completed successfully!")
        print(f"🎯 Ready for hackathon deployment with SQLite backend")
        
        # Load and display sample
        issues = load_issues_from_database()
        if issues:
            print(f"\n📋 Sample issue loaded:")
            print(f"   Failure: {issues[0]['Failure'][:80]}...")
            print(f"   Solution: {issues[0]['Solution'][:80]}...")
    else:
        print("\n❌ Database conversion failed - file not created")
        
    print("="*60)