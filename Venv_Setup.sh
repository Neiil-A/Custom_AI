#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Creating and activating virtual environment..."

# Check if the virtual environment already exists
if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo "Virtual environment created."
else
  echo "Virtual environment already exists."
fi

# Activate the virtual environment
source venv/bin/activate
echo "Virtual environment activated."

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt
echo "Dependencies installed."

# Check directory structure
echo "Checking directory structure..."
directories=( "agents" "data" "models" "tools" "tasks" )

for dir in "${directories[@]}"; do
  if [ ! -d "$dir" ]; then
    echo "Directory $dir does not exist. Creating it..."
    mkdir -p "$dir"
  else
    echo "Directory $dir exists."
  fi
done

# Create __init__.py files if not present
echo "Creating __init__.py files..."
for dir in "${directories[@]}"; do
  if [ ! -f "$dir/__init_
