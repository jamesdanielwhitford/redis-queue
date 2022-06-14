from crypt import methods
from unittest import result
from queue_app import app
from queue_app.tasks import scrape_url
from queue_app import q 
from flask import redirect, render_template, request, url_for
from time import strftime
from rq.job import Job
from queue_app.__init__ import r
import hashlib

@app.route("/")
def index():
    return render_template("add_task.html")



@app.route("/add_task", methods=["GET", "POST"])
def add_task():

    jobs = q.jobs


    message = None

    if request.args:
        url = request.args.get("url")

        job_id = hashlib.md5(url.encode()).hexdigest()
        
        q.enqueue(scrape_url, url, job_id = job_id, result_ttl=5000)

        return redirect(url_for(f"get_results", job_key=job_id))



    return render_template("add_task.html", message=message, jobs=jobs)

@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):

    q_len = len(q.jobs) + 1
    
    job = Job.fetch(job_key, connection=r)

    # Print errors to console
    if job.result[2]:
        print(job.result[2])

    if job.is_finished:
        return render_template("final.html", paragraphs=job.result[0], title = job.result[1]), 200
    else:
        return render_template("final.html", paragraphs=False, q_len=q_len), 202
