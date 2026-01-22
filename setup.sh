#!/bin/bash

echo "🚀 Starting ViktorHub Setup..."

# Backend Setup
echo "--- Setting up Backend ---"
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py makemigrations content
python3 manage.py migrate
python3 manage.py seed_data
echo "✅ Backend ready! Run 'source venv/bin/activate && python3 manage.py runserver' to start."

cd ..

# Frontend Setup
echo "--- Setting up Frontend ---"
cd frontend
rm -rf node_modules package-lock.json
npm install
echo "✅ Frontend ready! Run 'npm run dev' to start."

echo "🎉 Setup complete!"
