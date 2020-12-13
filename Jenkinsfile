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
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          script{
           groovyfile.build_app()
          }
        }
      }
    }

    stage ('Test App') {
      steps{
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
      }
    }
  }
}
