FROM python:3.8

# Copy Files

# COPY ./datasets /datasets
# COPY ./model-params/ /model-params
# COPY ./preprocessing/ /preprocessing

COPY Pipfile /
COPY Pipfile.lock /

COPY main.py /

# Install Dependencies

RUN pip3 install fastapi uvicorn
# RUN pipenv install --system --deploy

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]