from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from navigation import Link


link_document_online_viewer = Link(
    text = _("Raw"), tags=('new_window',),
    view="c4csap:document_online_viewer", args="object.pk"
)

link_document_version_online_viewer = Link(
    text = _("Raw"), tags=('new_window',),
    view="c4csap:document_version_online_viewer", args="object.pk"
)