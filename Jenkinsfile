#!groovy

def BuildDev() {
    timeout(120) {
        waitUntil {
            try {
                sh 'make build-dev'
                return true
            } catch (exception) {
                return false
            }
        }
    }
}

def StartDev() {
    timeout(120) {
        waitUntil {
            try {
                sh 'make start-dev-daemon'
                return true
            } catch (exception) {
                return false
            }
        }
    }
}

def StopDev() {
    timeout(120) {
        waitUntil {
            try {
                sh 'make stop-dev'
                return true
            } catch (exception) {
                return false
            }
        }
    }
}

def RunTest() {
    sh 'sudo docker-compose exec -T web python manage.py test deployer -v 2'
}

node {

    try {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"

        stage 'Test'
            sh 'cd /home/vagrant/projects/django/api-microserver/'
            BuildDev()
            StartDev()
            RunTest()
            StopDev()

        stage 'Deploy'
            sh 'ls'

        stage 'Publish results'
            slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
    }

    catch (err) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
        throw err
    }

}
