from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import polls_list, polls_details
from .apiviews import PollList, PollDetail
from .apiviewset import PollViewSet
from rest_framework.authtoken import views


from .apiviews_generic import (
    PollList as PollListGeneric,
    PollDetail as PollDetailGeneric,
    ChoiceList,
    CreateVote,
)

from .apiviews_generic_advanced import ChoiceList, CreateVote
from .apiview_gen_auth import (
    UserCreate,
    LoginView,
    PollViewSet as PollViewsetAuth,
    ChoiceList as ChoiceListAuth,
)

urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>", polls_details, name="polls_details"),
    #
    path("polls_api_view/", PollList.as_view(), name="polls_list_2"),
    path("polls_api_view/<int:pk>", PollDetail.as_view(), name="polls_detail_2"),
    #
    path("polls_gen_api_view/", PollListGeneric.as_view(), name="polls_list_2"),
    path(
        "polls_gen_api_view/<int:pk>",
        PollDetailGeneric.as_view(),
        name="polls_detail_2",
    ),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    #
    path(
        "poll_relations/<int:pk>/choices/",
        ChoiceList.as_view(),
        name="choice_list_advanced",
    ),
    path(
        "poll_relations/<int:pk>/choices/<int:choice_pk>/vote",
        CreateVote.as_view(),
        name="create_vote",
    ),
]


router = DefaultRouter()
router.register("polls_viewset", PollViewSet, basename="polls_viewset")
router.register("polls_viewset_auth/", PollViewsetAuth, basename="polls_viewset_auth")
# router.register("choices_auth/", ChoiceListAuth, basename="choice_list_auth")
#

urlpatterns += router.urls

urlpatterns.extend(
    [
        path("users/", UserCreate.as_view(), name="user_create"),
        path("login/", LoginView.as_view(), name="login"),
        # path("login/", views.obtain_auth_token, name="login"),
        #
    ]
)
