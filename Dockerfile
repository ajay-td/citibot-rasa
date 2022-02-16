FROM rasa/rasa:3.0.4
ENTRYPOINT []
USER root
ADD . /app/.
RUN ls /
RUN ls /app/scripts/

RUN python -m pip install --upgrade pip
RUN pip install sanic==21.6.0 Sanic-Cors==1.0.0 sanic-routing==0.7.0

RUN chmod +x /app/start_services.sh
RUN chmod +x /app/start_shell.sh
RUN pwd
RUN ls
CMD start_services.sh
