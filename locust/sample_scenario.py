from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):

    @task
    def hello_world(self):
        self.client.get("/")


class Locks(TaskSet):

    @task(7)
    def fast(self):
        self.client.get('/lock/fast')

    @task(3)
    def slow(self):
        self.client.get('/lock/slow')


class WebsiteUser(HttpLocust):
    task_set = Locks
    # min_wait = 5000
    # max_wait = 15000
