FROM ubuntu:latest
  
# Install Python Setuptools
Run apt-get update
Run apt-get install -y python3 python3-dev python3-pip
  
# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt
  
# Bundle app source
ADD . /src
  
# Expose
EXPOSE 5000
  
# Run
CMD ["python", "/src/app.py"]
