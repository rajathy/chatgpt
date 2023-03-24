pipeline {
  agent any
  environment {
    OPENAI_API_KEY = credentials('OPENAI_API_KEY')
  }
  stages {
    stage('hello') {
      steps {
        echo 'hello changed 2'
        echo $OPENAI_API_KEY
      }
    }

  }
}