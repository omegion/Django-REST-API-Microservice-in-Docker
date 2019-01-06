#!groovy

node {

    try {
        stage 'Checkout'
            sh 'ls'
            def lastChanges = readFile('GIT_CHANGES')
            slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"

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
