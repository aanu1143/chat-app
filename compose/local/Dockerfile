# Pull base image
FROM python:3.8.2
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


# Set work directory
WORKDIR /code
# Install dependencies

RUN pip install -r /requirements.txt

COPY ./compose/local/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Copy project
COPY . /code/