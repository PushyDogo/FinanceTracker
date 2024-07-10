pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git(url: 'https://github.com/PushyDogo/FinanceTracker', branch: 'dev')
            }
        }
    }
}