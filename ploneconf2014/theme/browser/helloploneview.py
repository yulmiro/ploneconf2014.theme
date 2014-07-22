from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from ploneconf2014.theme import themeMessageFactory as _


class IHelloPloneView(Interface):
    """
    HelloPlone view interface
    """

    def test():
        """ test method"""


class HelloPloneView(BrowserView):
    """
    HelloPlone browser view
    """
    implements(IHelloPloneView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        message = _(u'Hello World')
        company = _(u'Plone Fundation!!!')

        return {'message': message, 'company': company}
