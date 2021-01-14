FROM python:3.7

# Copy Files

COPY ./ /

# Install Dependencies

RUN pip3 install pipenv
RUN pipenv install 

EXPOSE 5000

CMD pipenv run python3 main.py