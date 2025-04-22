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
        // kill any stray python.exe
        bat 'taskkill /F /IM python.exe || exit 0'

        // fire off Flask in the background and pipe its output into flask.log
        bat 'start "flask-demo" /min cmd /c "cd /d %WORKSPACE% && call venv\\\\Scripts\\\\activate.bat && pythonw app.py > flask.log 2>&1"'
      }
    }
  }

  post {
    always {
      // make flask.log available under Artifacts
      archiveArtifacts artifacts: 'flask.log', allowEmptyArchive: true
    }
    success {
      echo '✅ Build succeeded!'
    }
    failure {
      echo '❌ Build failed!'
    }
  }
}
