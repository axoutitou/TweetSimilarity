def groovyfile

pipeline {
  agent any
  stages {
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

    stage ('Test App') {
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
    
    stage ('Push to Release') {
      steps{
        script{
            withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId:'fpa-alex', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
                  powershell('git remote set-url origin https://USERNAME:PASSWORD@github.com/axoutitou/TweetSimilarity.git')
                  powershell('git checkout origin Release')
           }
        }
      }
    }
  }
}
