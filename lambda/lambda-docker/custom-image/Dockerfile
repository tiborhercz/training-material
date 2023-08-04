ARG FUNCTION_DIR="/function"

FROM python:3.10 as build-image

ARG FUNCTION_DIR

RUN mkdir -p ${FUNCTION_DIR}
COPY . ${FUNCTION_DIR}

RUN pip install \
    --target ${FUNCTION_DIR} \
        awslambdaric numpy

FROM python:3.10-slim

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]

CMD [ "main.handler" ]
