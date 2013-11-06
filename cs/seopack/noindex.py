from plone.app.layout.viewlets import ViewletBase
from zope.component import getMultiAdapter
from Acquisition import aq_inner


class NoIndex(ViewletBase):

    def show(self):
        start = self.request.get('b_start', None)
        if start is not None:
            return False
        context = aq_inner(self.context)
        
        context_state = getMultiAdapter(
            (context, self.request), name=u'plone_context_state')
        
        if context_state.is_default_page():
            current_page_url = context_state.current_page_url()
        
            if context.absolute_url() == current_page_url:
                return True
            else:
                return False
        else:
            return False
