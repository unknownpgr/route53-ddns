# Set tag as git commit hash
TAG=$(git rev-parse --short HEAD)

# Define image name
IMAGE_TAGGED=unknownpgr/route53-ddns:$TAG
IMAGE_LATEST=unknownpgr/route53-ddns:latest

# Build docker image
docker build -t $IMAGE_TAGGED -t $IMAGE_LATEST .

# Push docker image
docker push $IMAGE_TAGGED
docker push $IMAGE_LATEST