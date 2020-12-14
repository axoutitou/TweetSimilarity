def build_app(){
  echo 'Prod branch is updating'
  bat 'docker-compose down'
  bat 'docker-compose up --build' 
}

def test_app(){
}

def down_app(){
}

def release_app(){
}

return this
