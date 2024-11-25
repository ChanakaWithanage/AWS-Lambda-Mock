
# Use AWS-provided base image for Python 3.12
FROM public.ecr.aws/lambda/python:3.12

# Copy the Lambda function code and requirements file into the container
COPY . /var/task/
# Install Python dependencies
RUN pip install -r /var/task/app/requirements.txt

# Expose debug port
EXPOSE 5678

# Set the Lambda handler (replace `lambda_function.lambda_handler` with your handler)
CMD ["app.lambda_function.lambda_handler"]
