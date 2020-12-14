def build_app(){
  echo 'Release branch is building and launching'
  bat 'docker-compose up -d'
}

def user_acceptance(){
 input "proceed with deployement to Prod?" 
}

def test_app(){
  echo 'Manual testing are executing'
  user_acceptance()
}

def down_app(){
  echo 'Application is shutting down'
  bat 'docker-compose down'
}

def release_app(){
    echo 'Merge into prod branch'             
    echo 'git remote set-url origin https://${USERNAME}:${PASSWORD}@github.com/axoutitou/TweetSimilarity.git'
    echo 'git checkout Prod'
    echo 'git merge Release'
    echo 'git push origin Prod'
}

return this
