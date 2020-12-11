def build_app(){
  echo 'Dev branch is building and launching'
  powershell 'docker-compose up -d'
}

def unit_test(){
  echo 'Unit tests are executing'
  powershell 'python test_app.py'
}


def integration_test(){
  echo 'Integration tests are executing'
  powershell 'python integration_tests_app.py'
}

def test_app(){
  echo 'Tests are executing'
  unit_test()
  integration_test()
}

def down_app(){
  echo 'Application is shutting down'
  powershell 'docker-compose down'
}

def release_app(){  
  
  withCredentials([usernamePassword(credentialsId: 'fpa-alex', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
    echo 'Merge into release branch'             
    powershell 'git remote set-url origin https://$USERNAME:$PASSWORD@github.com/axoutitou/TweetSimilarity.git'
    echo 'The user name is $USERNAME' 
    echo 'The password is $PASSWORD'
    powershell 'git checkout Release'
    powershell 'git merge Dev'
    powershell 'git push origin Release'
  }
}

return this
