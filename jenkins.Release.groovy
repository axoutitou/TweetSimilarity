def build_app(){
  echo 'Dev branch is building and launching'
  bat 'docker-compose up -d'
}

def test_app(){
  echo 'Tests are executing'
}

def down_app(){
  echo 'Application is shutting down'
  sh 'docker-compose down'
}

def release_app(){
}

return this
