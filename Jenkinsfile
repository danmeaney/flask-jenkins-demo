pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        bat 'python -m venv venv'
        bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
      }
    }

    stage('Lint') {
      steps {
        bat 'call venv\\Scripts\\activate && flake8 . --exclude=venv'
      }
    }

    stage('Test') {
      steps {
        bat 'call venv\\Scripts\\activate && pytest -q'
      }
    }

    stage('Deploy (demo)') {
      steps {
        // kill any stray Flask/python processes
        bat 'taskkill /F /IM python.exe || exit 0'

        // cd into workspace, activate venv, then start pythonw in the background
        // redirect both stdout & stderr into flask.log
        bat 'cd /d %WORKSPACE% && call venv\\Scripts\\activate && start "" /min pythonw app.py 1> flask.log 2>&1'
      }
    }
  }

  post {
    // make sure we always archive the log so you can inspect it
    always {
      archiveArtifacts artifacts: 'flask.log', fingerprint: true
    }
    success {
      echo 'Build succeeded!'
    }
    failure {
      echo 'Build failed.'
    }
  }
}
