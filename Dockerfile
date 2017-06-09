FROM eyevinntechnology/toolbelt:v4.4
MAINTAINER Eyevinn Technology <info@eyevinn.se>
RUN apt-get update && apt-get install -y --force-yes \
  curl
COPY entrypoint.py /root/entrypoint.py
ENTRYPOINT ["/root/entrypoint.py"]
CMD []
