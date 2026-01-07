from prefect import task

@task
def transform(data):
    extract_data = ['a','b','c']
    return extract_data