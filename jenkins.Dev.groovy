def build_app(){
  echo 'Dev branch is building and launching'
  bat 'docker-compose up -d'
}

def create_tests_env(){
  echo 'The testing environement is being created'
  bat 'docker build -f Dockerfile_tests -t tweets_similarity_tests .'
}

def run_tests(){
  echo 'Unit and integration tests are executing'
  bat 'docker run tweets_similarity_tests'
}


def destroy_tests_env(){
  echo 'Environement tests is being removed'
  bat 'docker rmi -f tweets_similarity_tests'
}

def test_app(){
  echo 'Tests are executing'
  create_tests_env()
  run_tests()
  destroy_tests_env()
}

def down_app(){
  echo 'Application is shutting down'
  bat 'docker-compose down'
}

def release_app(){  
  
  withCredentials([usernamePassword(credentialsId: 'fpa-alex', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
    echo 'Merge into release branch'             
    echo 'git remote set-url origin https://${USERNAME}:${PASSWORD}@github.com/axoutitou/TweetSimilarity.git'
    echo 'git checkout Release'
    echo 'git merge Dev'
    echo 'git push origin Release'
  }
}

return this
