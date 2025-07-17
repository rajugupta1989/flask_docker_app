pipeline {
    agent any

    options {
        timestamps()
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
                sh '''
                    if [ "$(docker ps -a -q -f name=flask-container)" ]; then
                        echo "Removing existing container..."
                        docker rm -f flask-container
                    else
                        echo "No existing container found."
                    fi
                '''
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
