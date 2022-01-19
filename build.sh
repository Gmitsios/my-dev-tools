export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0

docker build -t my-dev-tools .
docker build -f Dockerfile_brownie -t dev-tools-brownie .

alias dc="docker-compose"
alias devdc="docker-compose -f docker-compose.yml -f docker-compose.dev.yml"