import web
render = web.template.render('templates/')

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

class index:
	def GET(self):
		i = web.input(name=None)
		return render.index(i.name)

if __name__ == "__main__": app.run()