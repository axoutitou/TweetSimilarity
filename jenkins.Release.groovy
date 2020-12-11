def build_app(){
  echo 'Dev branch is building and launching'
  bat 'docker-compose up -d'
}

def user_acceptance(){
 input "proceed with deployement to Prod?" 
}

def test_app(){
  echo 'Tests are executing'
  user_acceptance()
}

def down_app(){
  echo 'Application is shutting down'
  bat 'docker-compose down'
}

def release_app(){
 withCredentials([usernamePassword(credentialsId: 'fpa-alex', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
    echo 'Merge into prod branch'             
    bat 'git remote set-url origin https://${USERNAME}:${PASSWORD}@github.com/axoutitou/TweetSimilarity.git'
    bat 'git checkout Prod'
    bat 'git merge Release'
    bat 'git push origin Prod'
  }
}

return this
