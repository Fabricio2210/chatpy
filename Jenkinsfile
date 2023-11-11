pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/Fabricio2210org/chatpy.git']]])
            }
        }

        stage('Build') {
            steps {
                sh 'pip install APScheduler chat-downloader schedule selenium'
            }
        }

        stage('Print Workspace') {
            steps {
                echo "Workspace directory: ${WORKSPACE}"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                script {
                    sh 'sudo systemctl restart chatpy'
                }
            }
        }
    }
}