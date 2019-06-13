FROM python:2.7-alpine

ENV LANG C.UTF-8

WORKDIR /apitests
ADD requirements.txt /apitests/
ADD bcdc_apitests /apitests/
ADD setup.py /apitests/
ADD LICENSE /apitests/
ADD MANIFEST.in /apitests/
ADD readme.md /apitests/

RUN ls -l /usr/local/bin
#RUN apk add --no-cache git
RUN cd /apitests && pip install -r /apitests/requirements.txt && pip install twine && python setup.py sdist bdist_wheel
ENV PYTHONPATH='/usr/lib/python2.7:/usr/lib/python2.7/site-packages:/apitests'
ENTRYPOINT ["/usr/local/bin/python", "-m", "twine", "upload", "dist/*", "-p", ${PYPI_PSWD}, "-u", ${PYPI_USER}]
