def groovyfile

pipeline {
  agent any
  
  parameters{
   booleanParam(name: "TestsOK", defaultValue: false); 
  }
  
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
         script{
            try {
               groovyfile.test_app()
               params.TestsOK = true
            } catch (Exception e) {
              
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
          script{
            if(params.TestsOK){
              groovyfile.release_app()
            }
         }
      }
    }
  }
}
