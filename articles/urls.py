from django.urls import path
from .views import acceuil,create_order,order_summary,page_erreur
from .views import register,user_login,user_beignet,user_fajita
from .views import index,proposer,detail,user_hemburger,mes_commandes,supprimer_commande


urlpatterns=[
    path("", index, name="index"),
      path("acceuil/",  acceuil, name="acceuil"),
      path("propos/",  proposer, name="propos"),
      path("detail/",  detail, name="detail"),
      path('register/', register, name="register"),
      path('login/',user_login, name="login"),
      path('create_order/', create_order, name='create_order'),
      path('order_summary/<int:order_id>/', order_summary, name='order_summary'),
      path('beignet/',user_beignet, name="beignet"),
      path('hemburger/',user_hemburger, name="hemburger"),
      path('fajita/',user_fajita, name="fajita"),
       path('mes_commandes/', mes_commandes, name='mes_commandes'),
       path('supprimer_commande/<int:commande_id>/', supprimer_commande, name='supprimer_commande'),
       path('page_erreur/', page_erreur, name='page_erreur'),
]