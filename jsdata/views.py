class JSDataViewMixin(object):

    def get_context_data(self, **kwargs):
        ctx = super(JSDataViewMixin, self).get_context_data(**kwargs)
        ctx['jsdata'] = self.get_jsdata()
        return ctx

    def get_jsdata(self, **kwargs):
        return kwargs
