pipeline {
    agent any

    options {
        timestamps()
    }

    triggers {
        // This enables the build trigger when GitHub sends a webhook
        githubPush()
    }

    stages {

        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
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
