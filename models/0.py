from gluon.storage import Storage
import sys

config = Storage(db=Storage(),
	auth=Storage(settings=Storage(extra_fields=Storage()),
		messages=Storage()),
	mail=Storage())

config.db.uri = "sqlite://contacts.sqlite"
config.db.check_reserved = ['all']

config.auth.settings.formstyle = 'divs'
config.auth.settings.registration_requires_verification = False
config.auth.settings.registration_requires_approval = False

config.auth.settings.extra_fields.auth_user = [
Field("avatar", "upload"),
Field("thumbnail", "upload")]

config.mail.server = 'smtp.gmail.com:587'
config.mail.sender = 'grupodesensoriamentoremoto@gmail.com'
config.mail.login = 'grupodesensoriamentoremoto@gmail.com:iemapm'

from gluon import current
current.config = config

#config app title, subtitle and menus

response.title = "Projeto DetecFeições"
response.subtitle = T("DetecFeições")

response.meta.author = "Rafael Soutelino"
response.meta.description = "detecfeicoes App"
response.meta.keywords = "web2py, python framework"
response.meta.generator = "web2py web framework"
response.meta.copyright = "Copyright 2012"
response.generic_patterns = ['*']


# from siodoc_plot import plot
# plot()
