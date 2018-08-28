Sample scripts for load testing demo
------------------------------------

Run applications (all start on the same address: http://localhost:5000/)::

   # Run async application
   $ vagga aiohttp

   # Run sync application:
   $ vagga flask


Running bencmark scripts::

   $ vagga ab
   $ vagga wrk
   $ vagga wrk2
   $ vagga locust
