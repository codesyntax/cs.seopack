from zope.component import getMultiAdapter
from Acquisition import aq_inner
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser import BrowserView
import urlparse

class CanonicalViewlet(ViewletBase):

    def canonical_url(self):
        context = aq_inner(self.context)
        view = getMultiAdapter((context, self.request), name="seopack_canonical_url")
        return view.canonical_url()

class CanonicalView(BrowserView):

    @property
    def pcs(self):
        context = aq_inner(self.context)
        return getMultiAdapter((context, self.request), 
                               name=u'plone_context_state') 

    def canonical_url(self):
        context = aq_inner(self.context)
        
        if self.pcs.canonical_object() is context:
            url = self.pcs.current_page_url()
            position = url.find('?')
            if position != -1:
                # Remove the trailing / just before the parameters
                if url[position-1] == '/':
                    url = url[:position-1] + url[position:]
            
            if url.endswith('/'):
                # Remove the trailing /
                url = url[:-1]
        else:
            url = self.pcs.canonical_object_url()
            qs = self.request.get('QUERY_STRING', '')
            if qs:
                url = url + '?' + qs
        
        return url

    def batch_url(self):
        canonical_url = self.canonical_url()
        return canonical_url.split('?')[0]

    def __call__(self, *args, **kwargs):
        return self.canonical_url()


class CanonicalBatchView(CanonicalView):
    def __call__(self, *args, **kwargs):
        return self.batch_url()
