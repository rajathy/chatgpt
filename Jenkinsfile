pipeline {
  agent any

  stages {
    stage('Identify new files') {
      steps {
        script {
          print "enterded here"
          bat 'git fetch --all'
          bat 'git diff-tree --no-commit-id --name-only -r HEAD|grep src/main/java > file'
          bat 'echo "identified files are : "'
          bat 'cat file'
        }
      }
    }

    stage('Generate Junits') {
      steps {
        script {
          bat 'pip3 install openai'
          bat 'python3 src/main/resources/chatgpt.py'
        }
      }
    }
    
    stage('clean up') {
      steps {
        script {
          bat 'rm file'
        }
      }
    }
    
  }
}
