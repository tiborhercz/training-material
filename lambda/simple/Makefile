build:
	rm -f lambda.zip
	pip3 install \
    --platform manylinux2014_x86_64 \
    --target=./package \
    --implementation cp \
    --python-version 3.11 \
    --only-binary=:all: --upgrade \
    -r requirements.txt
	cd package && zip -r ../lambda.zip .
	zip lambda.zip lambda_function.py

deploy:
	aws lambda update-function-code --function-name test --zip-file fileb://lambda.zip
