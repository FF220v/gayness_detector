# Artificially Intelligent Gay Detector
### Abstract:
- The product is a web server with a built-in artificial intelligence module
which purpose is to check if person is a gay or not.

### Features:
- You are capable of detecting gay by sending his name to a server.
- Server uses `Artificial intelligence (TM)` module to detect a gay.
- Gay data is stored in a redis database.
- User can acquire and share the data as the database is remote and accessed by HTTP

### How to use:
- The AI gay detector server is controlled by following http requests:

1. GET / - Get all acquired data
2. GET /object_id - Get a particular object by id
3. POST /object_id - Send an object for processing
4. POST /cleanup - Erase all items
5. DELETE /object_id - Delete a particular object by id


