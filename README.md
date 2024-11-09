## Description
number_to_french is a simple program that output the given number in French.

## Run
In the following two sections, we are describing how to run the run the program using uv and inside a Docker container.

### Using uv
This program is using `uv` package manager, you can [install it](https://docs.astral.sh/uv/getting-started/installation/) and run:
```bash
uv sync
uv run kata-number-to-french
```

You can override the default arguments, by passing -n option:
``` bash
uv run kata-number-to-french -n 123 456
````

to run the tests, execute:
```bash
uv run pytest
```

If you don't want to install uv, don't worry, we got you covered ;) ! Please follow the instruction in the next section.

### Using Docker
```bash
docker build . -t numbers_to_french
docker run numbers_to_french
```

ℹ️ In the Docker image we install the built wheel package and run using python -m.

Additionally, the run can take a list of numbers as argument, as:
``` bash
docker run numbers_to_french -n 123 456
````

And to run the tests, execute:
```bash
docker run --entrypoint uv numbers_to_french run pytest
```
