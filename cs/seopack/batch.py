from plone.app.layout.viewlets import ViewletBase

class BatchNoIndex(ViewletBase):

    def show(self):
        return self.request.get('b_start', 1) != 0

