pipeline {
  agent any
  environment {
    OPENAI_API_KEY = credentials('OPENAI_API_KEY')
  }
  stages {
    stage('hello') {
      steps {
        script {
          sh 'echo "from script"'
          sh 'echo ${OPENAI_API_KEY} >secretfile'
        }
      }
    }

  }
}