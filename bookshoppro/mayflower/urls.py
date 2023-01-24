from django.urls import path
from mayflower import views

urlpatterns=[
    path('indexpage/', views.indexpage, name="indexpage"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('savedata/', views.savedata, name="savedata"),
    path('display/', views.display, name="display"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatepage/<int:dataid>/', views.updatepage, name="updatepage"),
    path('deletepage/<int:dataid>/', views.deletepage, name="deletepage"),
    path('catpage/',views.catpage,name="catpage"),
    path('datasave/', views.datasave, name="datasave"),
    path('catdisplay/', views.catdisplay, name="catdisplay"),
    path('cateditpage/<int:dataid>/', views.cateditpage ,name="cateditpage"),
    path('catupdate/<int:dataid>/', views.catupdate, name="catupdate"),
    path('catdelete/<int:dataid>/', views.catdelete, name="catdelete"),
    path('cakepage/', views.cakepage, name="cakepage"),
    path('cakesave/', views.cakesave, name="cakesave"),
    path('cakedisplay/',views.cakedisplay,name="cakedisplay"),
    path('cakeedit/<int:dataid>/', views.cakeedit, name="cakeedit"),
    path('cakeupdate/<int:dataid>/', views.cakeupdate, name="cakeupdate"),
    path('cakedelete/<int:dataid>/', views.cakedelete, name="cakedelete"),
    path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
    path('adminlog/', views.adminlog, name="adminlog"),
    path('cntdispage/', views.cntdispage, name="cntdispage")
]

