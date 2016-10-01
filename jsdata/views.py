import re


url_prog = re.compile(r'\^([a-z/]+)(\(\?P<pk>\[\^/\.\]\+\)/)?([a-z/]*)\$')


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
        routers = self.get_router()
        if not isinstance(routers, list):
            routers = [routers]
        for router in routers:
            for url in router.urls:
                match = url_prog.match(url.regex.pattern)
                if not match:
                    continue
                api[url.name] = self.api_prefix + match.group(1)
                if match.group(2):
                    api[url.name] += '<pk>/'
                if match.group(3):
                    api[url.name] += match.group(3)
        api.update(kwargs)
        return api

    def get_router(self):
        raise NotImplemented
