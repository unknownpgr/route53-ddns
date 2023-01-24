# Set tag as git commit hash
TAG=$(git rev-parse --short HEAD)

# Define image name
IMAGE=unknownpgr/route53-ddns:$TAG

# Build docker image
docker build -t $IMAGE .

# Push docker image
docker push $IMAGE