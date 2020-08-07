#coding:utf-8
#
#需要预先安装gearman服务
#
"""
client： 提交任务    自行实现
service：分配任务    gearman实现
worker： 执行任务    自行实现
"""

####################################################################client
import gearman

gm_client = gearman.GearmanClient(['localhost:4730', 'otherhost:4730'])

# See gearman/job.py to see attributes on the GearmanJobRequest
# Defaults to PRIORITY_NONE, background=False (synchronous task), wait_until_complete=True
completed_job_request = gm_client.submit_job("task_name", "arbitrary binary data")
check_request_status(completed_job_request)




####################################################################worker
import gearman

gm_worker = gearman.GearmanWorker(['localhost:4730'])

# See gearman/job.py to see attributes on the GearmanJob
# Send back a reversed version of the 'data' string
def task_listener_reverse(gearman_worker, gearman_job):
    return reversed(gearman_job.data)

# gm_worker.set_client_id is optional
gm_worker.set_client_id('your_worker_client_id_name')
gm_worker.register_task('reverse', task_listener_reverse)

# Enter our work loop and call gm_worker.after_poll() after each time we timeout/see socket activity
gm_worker.work()



