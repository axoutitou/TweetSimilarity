def groovyfile

pipeline {
  agent any
  
  stage ('Build Script') {
    steps{
      script{
        def filename = 'jenkins.' + env.BRANCH_NAME + '.groovy'
        groovyfile = load filename
      }
    }
  }
  
  stage ('Build App') {
    steps{
      script{
        groovyfile.build_app()
     }
    }
  }
  
  stage ('Build App') {
    steps{
      script{
        groovyfile.test_app()
     }
    }
  }
  
  stage ('Down App') {
    steps{
      script{
        groovyfile.down_app()
     }
    }
  }
  
  stage ('Release App') {
    steps{
      script{
        groovyfile.release_app()
     }
    }
  }
  
}
