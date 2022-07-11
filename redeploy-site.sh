#!/bin/bash

#1)kill all existing tmux sessions, to ensure site is down
###tmux kill-server
#2) cd into project folder
cd /root/github-repositories/portfolio-website
#3)this command makes sure local repo has latest changes from main branch
#  on github.
git fetch && git reset origin/main --hard

#4)enter virtual environment and install dependencies
###source ./venv/bin/activate
###pip3 install -r requirements.txt

#5)start new detached tmux session and start flask server in virtual env
###SESSION="site-autodeploy"
###WINDOW=0                   #new sessions always have a 0 window
###tmux new -d -s $SESSION #create new detached session

#run command in the tmux window
#sends the key clicks and 'presses' enter
###tmux send-keys -t $SESSION:$WINDOW 'export FLASK_ENV=development' Enter
###tmux send-keys -t $SESSION:$WINDOW 'flask run --host=0.0.0.0' Enter

#new step since we created a systemd service
###systemctl restart myportfolio

#new steps since docker
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
exit 0