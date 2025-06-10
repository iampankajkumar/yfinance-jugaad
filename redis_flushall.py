import redis

# Connect to Redis (adjust host/port/db/password if needed)
r = redis.Redis(host='gusc1-cool-owl-30106.upstash.io', port=30106, password='0d7dbff6f4a54d10b9956ac9cf8a5215', ssl=True, decode_responses=True)

# WARNING: This deletes **everything** in Redis
r.flushall()

print("Redis has been completely cleaned.")
