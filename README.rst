Sample scripts for load testing demo
------------------------------------

Prerequisite: ``vagga`` — a containerization tool — https://vagga.readthedocs.io/en/latest/installation.html#ubuntu

Available vagga commands::

   $ vagga
   Available commands:
       ab                  Run ab
       aiohttp             Run sample aiohttp application
       aiohttp-socket      Run 4 instances of aiohttp app bound to the same address.
       bench               Run a set of tools ab/wrk/wrk2 one after other
       bench2              Run a set of tools wrk/wrk2 one after other
       flask               Run sample Flask application
       flask-gunicorn      Run sample Flask application with Gunicorn
       locust              Run Locust (http://localhost:8090)
       wrk                 Run wrk
       wrk2                Run wrk2

Test scenario: 

In one terminal run one of applications
(all start on the same address: http://localhost:5000/)::

   # Run async application
   $ vagga aiohttp

   # Run sync application:
   $ vagga flask
   
   # Run sync app in 4 processes
   $ vagga flask-gunicorn
   
   # Run async app in 4 processes (reuse socket address)
   $ vagga aiohttp-socket

In another terminal run bencmark scripts::

   $ vagga ab
   $ vagga wrk
   $ vagga wrk2
   $ vagga locust
   # Or preset commands:
   $ vagga bench
   $ vagga bench2
