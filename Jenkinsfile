pipeline {
  agent any

  stages {
    stage('Identify new files') {
      steps {
        script {
          print "enterded here"
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
          sh 'pip3 install openai'
          sh 'python3 src/main/resources/chatgpt.py'
        }
      }
    }
    
    stage('clean up') {
      steps {
        script {
          sh 'rm file'
        }
      }
    }
    
  }
}
