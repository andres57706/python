import sys
import redis

client = redis.Redis('localhost',6789,0)



def getall(name:str):
	out:dict = {}
	for i in client.hgetall(name).items():
		out[str(i[0], "utf-8")] = str(i[1],"utf-8")
	print(out)

def getkeys(name:str):
	print([ str(i, "utf-8") for i in client.hgetall(name).keys()])

def getkey(name:str, key:str):
	print(str(client.hget(name, key), "utf-8"))

def hset(name: str, jsonstr: str):
	from json import loads
	print(client.hset(name,mapping=loads(jsonstr)))

def hsetkey(name: str, key:str, value:str):
	print(client.hset(name, key, value))

def delete(name: str):
	print(client.delete(name))

if __name__ == "__main__":
	args = sys.argv[1::]
	# print(f"len args {args}")	
	if len(args) < 2:
		print("""
		USAGE:
		
		python -m hash [COMMAND] [ARGS]

		COMMANDS:
		getall		name
		getkey		name, key
		getkeys		name
		hset		name, jsonstringified
		hsetkey		name, key, value
		del			name
		""")
		sys.exit(1)
	if args[0] == "getall":
		getall(args[1])
		sys.exit(0)
	elif args[0] == "getkey":
		getkey(args[1], args[2])
		sys.exit(0)
	if args[0] == "getkeys":
		getkeys(args[1])
		sys.exit(0)
	elif args[0] == "hset":
		hset(args[1], args[2])
		sys.exit(0)
	elif args[0] == "hsetkey":
		hsetkey(args[1], args[2], args[3])
		sys.exit(0)
	elif args[0] == "del":
		delete(args[1])
		sys.exit(0)
	
	
# getall("pythondict")