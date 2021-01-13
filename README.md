A-maze-ingly Subito
===================

This program use the bfs (Breadth-first search) algorithm for traversing all graph data structure
and find a route to reach the word in the input list.

# Input

## Json input file

```
{
	"rooms": [{
			"id": 1,
			"name": "Hallway",
			"north": 2,
			"east": 7,
			"objects": []
		},
		{
			"id": 2,
			"name": "Dining Room",
			"north": 5,
			"south": 1,
			"west": 3,
			"east": 4,
			"objects": []
		},
		{
			"id": 3,
			"name": "Kitchen",
			"east": 2,
			"objects": [{
				"name": "Knife"
			}]
		},
		{
			"id": 4,
			"name": "Sun Room",
			"west": 2,
			"north": 6,
			"south": 7,
			"objects": []
		},
		{
			"id": 5,
			"name": "Bedroom",
			"south": 2,
			"east": 6,
			"objects": [{
				"name": "Pillow"
			}]
		},
		{
			"id": 6,
			"name": "Bathroom",
			"west": 5,
			"south": 4,
			"objects": []
		},
		{
			"id": 7,
			"name": "Living room",
			"west": 1,
			"north": 4,
			"objects": [{
				"name": "Potted Plant"
			}]
		}
	]
}
```

## Words List

The word list are a string separate by "," that is used to find a path. In the result table all word need to be present

## Node id
This is the item "id" node, write inside the json, used by program as root node.

# Running a program

## Run program

```
python <py program> <json file name> <root node id> <string list of word>
```

es.
```
python src/run.py tests/input_json/json_input_file.json 2 "Knife,Potted Plant"
```

## Run test

```
nosetests tests
```

## Running with Docker

### Build Image

```
docker build -t mytest .
```

### Run docker image with script

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