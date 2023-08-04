build:
	rm -f lambda.zip
	zip lambda.zip lambda_function.py

deploy:
	aws lambda update-function-code --function-name test --zip-file fileb://lambda.zip
