FROM rasa/rasa:3.0.4
ENTRYPOINT []
USER root
ADD ./scripts/* /scripts/
ADD . /app/
RUN ls /
RUN python -m pip install --upgrade pip
RUN pip install sanic==21.6.0 Sanic-Cors==1.0.0 sanic-routing==0.7.0
 
RUN chmod +x /scripts/*
CMD /scripts/start_services.sh
