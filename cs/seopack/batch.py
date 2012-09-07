from plone.app.layout.viewlets import ViewletBase

class BatchNoIndex(ViewletBase):

    def show(self):
        start = self.request.get('b_start', None)
        if start is None:
            return False
            
        try:
            b_start = int(start)
            return b_start != 0
        except ValueError:
            return False
        except TypeError:
            return False

        