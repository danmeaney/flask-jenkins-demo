pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup Python') {
      steps {
        bat 'python -m venv venv'
        bat 'call venv\\Scripts\\activate.bat && pip install -r requirements.txt'
      }
    }

    stage('Lint') {
      steps {
        bat 'call venv\\Scripts\\activate.bat && flake8 . --exclude=venv'
      }
    }

    stage('Test') {
      steps {
        bat 'call venv\\Scripts\\activate.bat && pytest -q'
      }
    }

    stage('Deploy (demo)') {
      steps {
        // kill any existing Python processes
        bat 'taskkill /F /IM python.exe || exit 0'
        // cd into the workspace, activate the venv, then launch Pythonw
        bat '''
          cd /d "%WORKSPACE%"
          call venv\\Scripts\\activate.bat
          pythonw app.py 1> flask.log 2>&1
        '''
      }
    }
  }

  post {
    // always grab the log even on success so you can inspect it
    always {
      archiveArtifacts artifacts: 'flask.log', fingerprint: true
    }
    success { echo 'Build succeeded!' }
    failure { echo 'Build failed.' }
  }
}
