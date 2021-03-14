FROM python:3.8


# Test comment.

MAINTAINER test



LABEL multi.label1="value1" multi.label2="value2" other="value3"
LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
LABEL multi.label1="value1" \
      multi.label2="value2" \
      other="value3"




COPY Dockerfile ./

RUN ["powershell", "-command", "Execute-MyCmdlet", "-param1 \"c:\\foo.txt\""]

CMD ["python"]