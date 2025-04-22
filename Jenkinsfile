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
        // kill any stray python
        bat 'taskkill /F /IM python.exe || exit 0'
        // start Flask headless and log to flask.log
        bat """
          cd /d %WORKSPACE% && ^
          call venv\\Scripts\\activate && ^
          start "" /min pythonw app.py 1> flask.log 2>&1
        """
      }
    }
  }

  post {
    // always archive flask.log whether build passes or fails
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
