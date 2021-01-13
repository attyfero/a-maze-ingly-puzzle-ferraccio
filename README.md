A-maze-ingly Subito
===================

All run are from the root directory of the project

# Run program

```
python src/run.py tests/input_json/json_input_file.json 2 "Knife,Potted Plant"
```

# Run test

```
nosetests tests
```

# Docker

## Build Image

```
docker build -t mytest .
```

## Run docker image with script

This command:

- mount all project in /mnt 
- set the workdir to /mnt 
- load image mytest
- run a script inside "scripts" directory project

```
docker run -v $(pwd):/mnt -w /mnt mytest ./scripts/run.sh
docker run -v $(pwd):/mnt -w /mnt mytest ./scripts/tests.sh
```

**IMPORTANT** the -p parameter is omitted because this is not for a network accesible service