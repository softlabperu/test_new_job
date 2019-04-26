TEST NEW JOB
=====

Build image docker
-----
`docker build -t test_new_job:latest -f docker/Dockerfile .`

Run container
-----
`docker run --name test -d -p 80:80 test_new_job:latest`
