#!groovy

node {

    try {
        stage 'Checkout'
            sh 'ls'
            slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`"

        stage 'Test'
            sh 'ls'

        stage 'Deploy'
            sh 'ls'

        stage 'Publish results'
            sh 'ls'
    }

    catch (err) {

        throw err
    }

}
