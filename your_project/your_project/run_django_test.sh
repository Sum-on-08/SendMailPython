#!/bin/bash

# Move into the Django project directory
# shellcheck disable=SC2164
cd /home/sumon/sendmail/your_project

# Activate virtual environment
source venv/bin/activate

# Start Django server in the background
python manage.py runserver 127.0.0.1:8000 &
SERVER_PID=$!

# Wait for the server to start
sleep 5

# Hit the test endpoint
#curl http://127.0.0.1:8000/api/test/
curl_response=$(curl -s http://127.0.0.1:8000/api/test/)
echo "Curl response: $curl_response"

# Kill the server after the request
kill $SERVER_PID
