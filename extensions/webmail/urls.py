from django.conf.urls.defaults import *

urlpatterns = patterns(
    'modoboa.extensions.webmail.views',
    (r'^$', "index"),
    (r'^submailboxes', "submailboxes"),
    (r'^getmailcontent', 'getmailcontent'),
    (r'^unseenmsgs', 'check_unseen_messages'),
    
    (r'^delete/$', 'delete'),
    (r'^move/$', "move"),
    (r'^mark/(?P<name>.+)/$', "mark"),
    (r'^empty/(?P<name>.+)/$', "empty"),
    (r'^compact/(?P<name>.+)/$', "compact"),
    (r'^newfolder/$', "newfolder"),
    (r'^editfolder/$', 'editfolder'),
    (r'^delfolder/$', 'delfolder'),
    
    (r'^attachments/$', 'attachments'),
    (r'^delattachment/$', 'delattachment'),
    
    (r'^(?P<folder>.+)/(?P<mail_id>[\w\-\+]+)/part/$', 'getattachment'),
    )
