from customer.models import Job
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


def get_jobs():
	jobs = Job.objects.all().order_by('-id')
	return jobs


def get_job(slug):
	job = Job.objects.get(slug=slug)
	return job

def get_jobs_by_category(category):
	jobs = Job.objects.filter(category=category).order_by('-id')
	return jobs

def get_job_locations(objects):
	locations = []
	for job in objects:
		locations.append(job['location'])
	return set(locations)

def get_job_companies(objects):
	companies = []
	for job in objects:
		companies.append(job['company'])
	return set(companies)


def paginate(objects,page):
	paginator = Paginator(objects,10)
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	return objects