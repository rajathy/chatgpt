pipeline {
  agent any

  stages {
    stage('Identify new files') {
      steps {
        script {
          sh 'git fetch --all'
          sh 'git diff-tree --no-commit-id --name-only -r HEAD|grep src/main/java > file'
          sh 'echo "identified files are : "'
          sh 'cat file'
        }
      }
    }

    stage('Generate Junits') {
      steps {
        script {
          sh 'python3 src/main/resources/chatgpt.py'
        }
      }
    }
  }
}