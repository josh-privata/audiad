# Dockerfile
# FROM directive instructing base image to build upon
FROM python:3.5.3
WORKDIR /usr/src/app
RUN mkdir /tmp/cer
RUN chmod 777 /tmp/cer
# COPY startup script into known file location in container
COPY start.sh ./
COPY requirements.txt ./
COPY mydatabase ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000
# CMD specifcies the command to execute to start the server running.
CMD ["./start.sh"]
# done!