FROM ubuntu:latest
  
# Install Python Setuptools
Run apt-get update
Run apt-get install -y python3 python3-dev python3-pip
# Bundle app source
RUN mkdir /src
ADD . /src
# Add and install Python modules
RUN cd /src; pip3 install -r requirements.txt
  
# Expose
EXPOSE 5000
  
# Run
CMD ["python3", "/src/app.py"]
