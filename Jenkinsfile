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
        // Kill any stray python processes
        bat 'taskkill /F /IM python.exe || exit 0'

        // Launch Flask in a new, minimized cmd window and capture logs
        bat '''
          start "flask-demo" /min cmd /c ^
            "cd /d %WORKSPACE% && ^
             call venv\\Scripts\\activate.bat && ^
             pythonw app.py > flask.log 2>&1"
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
    always {
      // Archive the flask.log so you can download it from the build page
      archiveArtifacts artifacts: 'flask.log', allowEmptyArchive: false
    }
  }
}
