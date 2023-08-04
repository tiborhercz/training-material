FROM python:3.11 as build

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.11-slim AS final-image
COPY --from=build /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY main.py /app

CMD python /app/main.py
