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
<<<<<<< HEAD
        script{
          groovyfile.build_app()
       }
=======
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          script{
           groovyfile.build_app()
          }
        }
>>>>>>> Dev
      }
    }

    stage ('Test App') {
      steps{
<<<<<<< HEAD
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
=======
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          script{
           groovyfile.test_app()
          }
        }
      }
    }
    
    stage ('Down App') {
      steps{
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          script{
           groovyfile.down_app()
          }
        }
      }
    }
    
   stage ('Release App') {
      steps{
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          script{
           groovyfile.release_app()
          }
        }
>>>>>>> Dev
      }
    }
  }
}
