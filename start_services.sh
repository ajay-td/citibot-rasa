
rasa run actions --actions actions&

rasa run -m /app/models/ --enable-api --cors "*" \
        --endpoints /app/endpoints.yml \
       
