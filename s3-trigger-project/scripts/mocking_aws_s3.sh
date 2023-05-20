#! /bin/sh

aws s3 mb s3://example-bucket --endpoint-url=http://localstack:4566
aws s3 cp /data/image.jpeg s3://example-bucket/image.jpeg --endpoint-url=http://localstack:4566
