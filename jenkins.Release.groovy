def build_app(){
  echo 'Dev branch is building and launching'
  powershell 'docker-compose up -d'
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
  powershell 'docker-compose down'
}

def release_app(){
}

return this
