import redis

r = redis.Redis(host="localhost", port=6379)
r.set("name", "redis")
print(r["name"])
print(r.get("name"))
print(type(r.get("name")))
