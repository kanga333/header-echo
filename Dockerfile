FROM python:2.7

RUN mkdir /app
COPY files/echo_server.py /app
RUN chmod +x /app/echo_server.py

EXPOSE 80 80

CMD ["/usr/local/bin/python","/app/echo_server.py"]