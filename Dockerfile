FROM ubuntu:12.10
  
# Install Python Setuptools
Run apt-get install python3 python3-dev python3-pip
  
# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt
  
# Bundle app source
ADD . /src
  
# Expose
EXPOSE 5000
  
# Run
CMD ["python", "/src/app.py"]
