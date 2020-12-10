def build_app(){
  echo 'Dev branch is building and launching'
  bat 'docker-compose up -d'
}

def test_app(){
  echo 'Tests are executing'
  bat 'python test_app.py
}

def down_app(){
  echo 'Application is shutting down'
  sh 'docker-compose down'
}

def release_app(){
  echo 'Branch into release'
}

return this
