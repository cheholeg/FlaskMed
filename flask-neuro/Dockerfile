FROM python:3.11.3  
MAINTAINER NIKITA FILIPPOV 'serfil1970@gmail.com'
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]