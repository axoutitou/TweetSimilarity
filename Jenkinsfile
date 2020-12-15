def groovyfile

def testsOK = 'false'

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
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          script{
           //groovyfile.build_app()
            echo '.'
          }
        }
      }
    }

    stage ('Test App') {
      steps{
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
         script{
            try {
             //  groovyfile.test_app()
               env.testsOK = 'true'
              echo '.'
            } catch (err) {
               error("Tests failed")
            }
         }
         }
      }
    }
    
    stage ('Down App') {
      steps{
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          script{
          // groovyfile.down_app()
            echo '.'
          }
        }
      }
    }
    
    stage ('Release App') {
      steps{
          script{
            if(env.testsOK == 'true'){
              groovyfile.release_app()
            }
         }
      }
    }
  }
}
