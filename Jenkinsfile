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
        bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
      }
    }

    stage('Lint') {
      steps {
        bat '.\\venv\\Scripts\\activate && flake8 . --exclude=venv'
      }
    }

    stage('Test') {
      steps {
        bat '.\\venv\\Scripts\\activate && pytest -q'
      }
    }

    stage('Deploy (demo)') {
      steps {
        // Kill any existing Python instances
        bat 'taskkill /F /IM python.exe || exit 0'

        // Launch Flask in a new, minimized window that stays alive
        bat """
          start "flask-demo" /min cmd /c ^
            "cd %WORKSPACE% && ^
             call venv\\Scripts\\activate.bat && ^
             python app.py"
        """
      }
    }
  }

  post {
    success { echo "Build succeeded!" }
    failure { echo "Build failed." }
  }
}
