from django.shortcuts import render, Http404
from home.models import Paste


def index(request, name=""):
	if name=="":
		return create(request)
	else:
		try :
			paste = Paste.objects.get(name=name)
		except Paste.DoesNotExist:
			raise Http404
	return render(request, 'home/index.html', locals())

def create(request):
	if request.method == "POST":
		if "code" not in request.POST:
			return render(request, "home/create.html", locals())
		else:
			code = request.POST["code"]
			if len(code) == 0:
				return render(request, "home/create.html", {})
			name = get_next_hash()
			paste = Paste.objects.create(name=name, code=code)
			paste.save()
			return index(request, name)
	else:
		return render(request, "home/create.html", locals())

def get_next_hash():
	try:
		paste = Paste.objects.latest('pk')
		name = paste.name
	except:
		name = "AAAAA"
	i = len(name)-1
	while (i > 0):
		if ord(name[i]) < ord("Z"):
			name = name[:i] + chr( ord(name[i])+1) + name[i+1:]
			break
		else:
			name = name[:i] + "A" + name[i+1:]
			i-=1
	if i == -1:
		name = name + "A"
	return name
