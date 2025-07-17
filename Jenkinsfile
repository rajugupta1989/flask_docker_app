pipeline {
    agent any

    options {
        timestamps() // Show timestamps in console log
    }

    stages {

        stage('Declarative: Checkout SCM') {
            steps {
                git url: 'https://github.com/rajugupta1989/flask_docker_app.git', branch: 'main'
            }
        }

        stage('Docker Build') {
            steps {
                echo '🔧 Building Docker image...'
                sh 'docker build -t flask-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo '🛑 Stopping old container if exists...'
                sh 'docker rm -f flask-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                echo '🚀 Running new Docker container...'
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }

    }

    post {
        always {
            echo '✅ CI/CD pipeline run complete.'
        }
    }
}