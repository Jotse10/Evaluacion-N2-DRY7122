pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clona el repositorio de GitHub
                git url: 'https://github.com/Jotse10/Evaluacion-N2-DRY7122.git', branch: 'master'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Construye la imagen Docker a partir del Dockerfile ubicado en el repositorio
                sh 'docker build -t sample-app .'
            }
        }
        stage('Deploy') {
            steps {
                // Si existe un contenedor anterior, se elimina
                sh 'docker rm -f sample-app || true'
                // Arranca el contenedor mapeando el puerto 9999 del contenedor al 9999 del host
                sh 'docker run -d -p 9999:9999 --name sample-app sample-app'
            }
        }
    }
    post {
        always {
            echo "Pipeline completado - Trabajo-Eva2 finalizado"
        }
    }
}


