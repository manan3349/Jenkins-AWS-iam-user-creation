pipeline {
    //By default, Use any Available Agent
    agent any

    //Declaring Parameters for Pipeline
    parameters {
        string(name: 'IAM_USER_NAME', description: 'AWS IAM Username.')
        choice(choices: ['Developer', 'Admin', 'Random'], name: 'IAM_Group', description: 'Select one group to add user.')
        text(name: 'SSH_Key', description: 'Provide SSH Public key to IAM user.')
    }
    
    stages{
        stage('GitHub code Download') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'bffa42dc-029f-40dd-835f-79b0f0d92d01', passwordVariable: 'token', usernameVariable: 'authd')]) {
                sh 'sudo curl -H "Authorization: token $token" -H "Accept: application/vnd.github.v3.raw" -o aws_access.py https://raw.githubusercontent.com/To-TheNew/Script/main/aws_access.py'
            }
        }
    }
        // Add collaborator in github.
        stage('Python Code') {
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'jenkins-aws-iam', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                sh 'python3 aws_access.py ${IAM_USER_NAME} ${IAM_Group} ${SSH_Key}'
                }
            }
        }
    }
}
