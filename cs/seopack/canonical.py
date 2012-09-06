from zope.component import getMultiAdapter
from Acquisition import aq_inner
from plone.app.layout.viewlets import ViewletBase

class CanonicalViewlet(ViewletBase):

    @property
    def pcs(self):
        context = aq_inner(self.context)
        return getMultiAdapter((context, self.request), 
                               name=u'plone_context_state') 

    def canonical_url(self):
        context = aq_inner(self.context)
        
        if self.pcs.canonical_object() is context:
            url = self.pcs.current_page_url()
        else:
            url = self.pcs.canonical_object_url()
            qs = self.request.get('QUERY_STRING', '')
            if qs:
                url = url + '?' + qs
        
        return url
