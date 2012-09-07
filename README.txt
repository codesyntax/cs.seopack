Introduction
============

This product adds some viewlet to improve SEO in Plone sites:

 - Meta tag to tell robots "noindex, follow" the batch pages

 - Canonical url link for all pages. We have followed these rules for canonical urls:

    - For normal content, the url is the object's url without the trailing '/':

        - yoursite.com/news/ -> yoursite.com/news

    - Default page (and its trailing '/') is removed from the canonical url:

        - yoursite.com/news/aggregator -> yoursite.com/news (aggregator is the default page of news)
        - yoursite.com/news/aggregator/ -> yoursite.com/news (aggregator is the default page of news)
    
    - View or template name is preserved in the canonical url:

        - yoursite.com/@@search?SearchableText=query -> yoursite.com/@@search?SearchableText=query
        - yoursite.com/folder1/folder_listing -> yoursite.com/folder1/folder_listing

 - Customized batching template to create batching base urls based on canonical urls.

Tested with Plone 4.2.x. It should work all previous Plone 4 versions, but it's untested. 

In Plone 4.3.x the changes in batching template will not be available, because of the
use of plone.batching product and this product provides replacement just for batch_macros.pt
template.


