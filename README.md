Eval.AI submission

    # Install EvalAI command line interface
    pip install evalai

    # Set EvalAI account token
    evalai set_token <your EvalAI participant token>

    # Push docker image to EvalAI docker registry
    evalai push multimediate-next-speaker:latest --phase <phase-id>



Build image:

    sudo docker build -f EyeContact.Dockerfile -t multimediate-test .
    sudo docker build -f NextSpeaker.Dockerfile -t multimediate-test .

Test image:

    sudo docker run -it --rm -v $PWD/input:/input -v $PWD/output:/output multimediate-test

Remove stopped containers

    sudo docker rm $(sudo docker ps -a -q)
