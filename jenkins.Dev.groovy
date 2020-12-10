def build_app(){
  echo 'Dev branch is building and launching'
  bat 'docker-compose up -d'
}

def unit_test(){
  echo 'Unit tests are executing'
  bat 'python test_app.py'
}


def integration_test(){
  echo 'Integration tests are executing'
  bat 'python integration_tests_app.py'
}

def test_app(){
  echo 'Tests are executing'
  unit_test()
  integration_test()
}

def down_app(){
  echo 'Application is shutting down'
  sh 'docker-compose down'
}

def release_app(){
  echo 'Branch into release'
}

return this
