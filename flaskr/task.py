from .extensions import scheduler


@scheduler.task('interval', id='do_job_1', seconds=10)
def task():
    print('执行任务...')
