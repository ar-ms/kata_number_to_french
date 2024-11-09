FROM python:3.13.0-bullseye

RUN pip install uv

RUN pip install --upgrade uv

COPY . /workspace

WORKDIR /workspace

RUN uv build

RUN pip install ./dist/kata_number_to_french-0.1.0-py3-none-any.whl

ENTRYPOINT [ "python", "-m", "kata_number_to_french", "-n" ]

CMD ["0", "1", "5", "10", "11", "15", "20", "21", "30", "35", "50", "51", "68", "70", "75", "99", "100", "101", "105", "111", "123", "168", "171", "175", "199", "200", "201", "555", "999", "1000", "1001", "1111", "1199", "1234", "1999", "2000", "2001", "2020", "2021", "2345", "9999", "10000", "11111", "12345", "123456", "654321", "999999"]
