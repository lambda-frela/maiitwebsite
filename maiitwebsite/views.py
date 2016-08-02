from django.shortcuts import render, render_to_response 
from club.models import *
from . import utils
from django.template import RequestContext
from django.db.models import Q

def events(request):
	template_name = 'index.html'

	events = Event.objects.all()

	paginate_by = 5
	page = request.GET.get('page')
	show_pages_delta = 5
	
	total_num_pages = 0
	event_list, page_range, total_num_pages = utils.paginated_list(page, paginate_by, show_pages_delta, events)
	return render_to_response(template_name, { "event_list": event_list, "page_range": page_range, "total_pages":total_num_pages }, context_instance=RequestContext(request))

def index(request):
	return about(request)

def partners(request):
	template_name = 'partners.html'
	partners = Partner.objects.all()
	return render_to_response(template_name, { "partner_list": partners }, context_instance=RequestContext(request))


def projects(request):
	template_name = 'projects.html'

	projects = Project.objects.all()

	paginate_by = 5
	page = request.GET.get('page')
	show_pages_delta = 5
	
	total_num_pages = 0
	project_list, page_range, total_num_pages = utils.paginated_list(page, paginate_by, show_pages_delta, projects)
	return render_to_response(template_name, { "project_list": project_list, "page_range": page_range, "total_pages":total_num_pages }, context_instance=RequestContext(request))


def members(request):
	template_name = 'members.html'
	team = Member.objects.filter( Q(member_type='org') | Q(member_type='lec') )
	return render_to_response(template_name, { "team_list":team }, context_instance=RequestContext(request))



def about(request):
	return render_to_response('about.html', RequestContext(request))

def handler404(request):
	response = render_to_response('404.html', {},
		context_instance=RequestContext(request))
	response.status_code = 404
	return response


def handler500(request):
	response = render_to_response('500.html', {},
		context_instance=RequestContext(request))
	response.status_code = 500
	return response


