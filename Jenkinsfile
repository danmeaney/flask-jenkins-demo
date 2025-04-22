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
        // kill any stray Python processes so we start fresh
        bat 'taskkill /F /IM python.exe || exit 0'

        // cd into workspace, activate venv, then launch Flask in a new, minimized cmd window
        // redirect stdout & stderr into flask.log
        bat 'cd /d %WORKSPACE% && call venv\\Scripts\\activate && start "flask-demo" /min cmd /C "python app.py >> flask.log 2>&1"'
      }
    }
  }

  post {
    // always grab the log so you can see what happened
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
