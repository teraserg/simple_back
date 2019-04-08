# import multiprocessing

proc_name = 'simple_back'
bind = "0.0.0.0:8000"
# workers = (2 * multiprocessing.cpu_count()) + 1
workers = 1
worker_class = 'aiohttp.worker.GunicornWebWorker'
max_requests = 200000
preload_app = True
reload = True
timeout = 600
