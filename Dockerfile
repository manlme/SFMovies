FROM ubuntu:latest
  
# Install Python Setuptools
Run apt-get update
Run apt-get install -y python3 python3-dev python3-pip
# Add and install Python modules
RUN mkedir /src
RUN cd /src; pip3 install -r requirements.txt
  
# Bundle app source
ADD . /src
  
# Expose
EXPOSE 5000
  
# Run
CMD ["python3", "/src/app.py"]
