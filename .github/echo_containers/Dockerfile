FROM alpine:3.20
WORKDIR /echo
COPY . /echo
CMD ["sh", "-c", "echo '[ECHO] Listing /echo && env'; ls -R /echo | head -n 50; env | sort | head -n 50"]
