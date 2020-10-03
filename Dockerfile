FROM jupyter/scipy-notebook

RUN pip install sklearn-pandas utils
RUN pip install Faker
