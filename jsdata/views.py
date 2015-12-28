import re


url_prog = re.compile(r'\^([a-z/]+)(\(\?P<pk>\[\^/\.\]\+\)/)?\$')


class JSDataViewMixin(object):

    def get_context_data(self, **kwargs):
        ctx = super(JSDataViewMixin, self).get_context_data(**kwargs)
        ctx['jsdata'] = self.get_jsdata()
        return ctx

    def get_jsdata(self, **kwargs):
        return kwargs


class DRFViewMixin(JSDataViewMixin):

    def get_jsdata(self, **kwargs):
        data = {'api': self.get_api()}
        data.update(kwargs)
        return data

    def get_api(self, **kwargs):
        api = {}
        router = self.get_router()
        for url in router.urls:
            match = url_prog.match(url.regex.pattern)
            if not match:
                continue
            api[url.name] = self.api_prefix + match.group(1)
            if match.group(2):
                api[url.name] += '<pk>/'
        api.update(kwargs)
        return api

    def get_router(self):
        raise NotImplemented
