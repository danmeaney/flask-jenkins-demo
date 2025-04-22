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
        // Create virtualenv and install dependencies
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
        // Kill any old Python processes
        bat 'taskkill /F /IM python.exe || exit 0'

        // Start Flask in background via pythonw and capture logs
        bat '''
          cd %WORKSPACE% && ^
          call venv\\Scripts\\activate.bat && ^
          start "" /min pythonw app.py > flask.log 2>&1
        '''
      }
    }
  }

  post {
    success {
      echo "Build succeeded!"
    }
    failure {
      echo "Build failed."
    }
  }
}
