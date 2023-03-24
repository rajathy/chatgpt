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
          sh 'echo $OPEN[AI_API_KEY}'
        }
      }
    }

  }
}