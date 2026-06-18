# MCP Auto-Fix Project

## Overview
This project demonstrates an automated bug detection and fixing system using Python, scheduler, and Git workflow.

## Problem
A Python program was created with a division by zero error.

## Solution
A scheduler monitors error logs and triggers an MCP-style automation script to fix the code automatically.

## Workflow
1. Buggy Python program created
2. Error generated (ZeroDivisionError)
3. Error logged in error.log
4. Scheduler detects error
5. MCP server simulates AI fix
6. Code is updated automatically
7. Changes committed using Git
8. Pull Request created on GitHub

## Files
- calculator.py
- scheduler.py
- mcp_server.py
- error.log

## Result
The system successfully handles errors and demonstrates automated debugging workflow.