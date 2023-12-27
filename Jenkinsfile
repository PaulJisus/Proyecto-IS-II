pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/desarrollo']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/PaulJisus/Proyecto-IS-II.git']]])
            }
        }
        stage('SonarQube analysis') {
            environment{
            def scannerHome = tool name: 'sonar_scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation';}
            steps{
            withSonarQubeEnv('SonarQube') { 
              bat "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
        stage('Build') {
            steps {
                git branch: 'desarrollo', url: 'https://github.com/PaulJisus/Proyecto-IS-II.git'
                bat 'python3 app.py'
            }
        }
        stage('Test unitario') {
            steps {
                git branch: 'desarrollo', url: 'https://github.com/PaulJisus/Proyecto-IS-II.git'
                bat 'python3 test/unitarias/test_model.py'
            }
        }
        stage('Test funcional') {
            steps {
                git branch: 'desarrollo', url: 'https://github.com/PaulJisus/Proyecto-IS-II.git'
                bat 'python3 test/funcionales/test_create_evento.py'
            }
        }
    }
}