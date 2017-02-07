from django.conf.urls import url
import views

urlpatterns = [
	url(r'^contact/$', views.contact),
    url(r'^allcategorys' , views.show_all_categorys),
    url(r'^posts/(?P<id>[0-9]+)/show_posts$'  , views.show_posts ),
    url(r'posts/(?P<id>[0-9]+)/details$'  , views.details ),
    # url(r'^questions/new',views.new_question),
    # url(r'^questions/(?P<id>[0-9a-z]+)/delete$'  , views.delete_ques )
    url(r'^pnew/$',views.Post_new),
    #url(r'^(?P<question_id>[0-9]+)/qdel/$',views.question_delete),
    #url(r'^(?P<question_id>[0-9]+)/qupdate/$',views.question_update),
   # (r'^accounts/login/$', login),
	#(r'^accounts/logout/$', logout),
]
