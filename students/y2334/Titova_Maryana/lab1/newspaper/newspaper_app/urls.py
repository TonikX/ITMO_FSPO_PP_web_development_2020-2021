from django.urls import path

from . import views
from .views import *


urlpatterns = [
   path('main/', views.getMain),

   path('PostOffice/PostOfficeView/', ViewAllPostOffices.as_view()),
   path('PostOffice/PostOfficeCreate/', AddPostOffices.as_view()),
   path('PostOffice/PostOfficeEdit/<int:id_post_office>', EditPostOffices.as_view()),
   path('PostOffice/PostOfficeDelete/<int:id_post_office>', DeletePostOffices.as_view()),

   path('EditorialOffice/EditorialOfficeView/', ViewAllEditorialOffices.as_view()),
   path('EditorialOffice/EditorialOfficeCreate/', AddEditorialOffices.as_view()),
   path('EditorialOffice/EditorialOfficeEdit/<int:id_editorial_office>', EditEditorialOffices.as_view()),
   path('EditorialOffice/EditorialOfficeDelete/<int:id_editorial_office>', DeleteEditorialOffices.as_view()),

   path('Newspaper/NewspaperView/', ViewAllNewspapers.as_view()),
   path('Newspaper/NewspaperCreate/', AddNewspapers.as_view()),
   path('Newspaper/NewspaperEdit/<int:id_newspaper>', EditNewspapers.as_view()),
   path('Newspaper/NewspaperDelete/<int:id_newspaper>', DeleteNewspapers.as_view()),

   path('PrintingOffice/PrintingOfficeView/', ViewAllPrintingOffices.as_view()),
   path('PrintingOffice/PrintingOfficeCreate/', AddPrintingOffices.as_view()),
   path('PrintingOffice/PrintingOfficeEdit/<int:id_printing_office>', EditPrintingOffices.as_view()),
   path('PrintingOffice/PrintingOfficeDelete/<int:id_printing_office>', DeletePrintingOffices.as_view()),

   path('Release/ReleaseView/', ViewAllReleases.as_view()),
   path('Release/ReleaseCreate/', AddReleases.as_view()),
   path('Release/ReleaseEdit/<int:id_release>', EditReleases.as_view()),
   path('Release/ReleaseDelete/<int:id_release>', DeleteReleases.as_view()),

   path('Article/ArticleView/', ViewAllArticles.as_view()),
   path('Article/ArticleCreate/', AddArticles.as_view()),
   path('Article/ArticleEdit/<int:id_article>', EditArticles.as_view()),
   path('Article/ArticleDelete/<int:id_article>', DeleteArticles.as_view()),

   path('Correction/CorrectionView/', ViewAllCorrections.as_view()),
   path('Correction/CorrectionCreate/', AddCorrections.as_view()),
   path('Correction/CorrectionEdit/<int:id_correction>', EditCorrections.as_view()),
   path('Correction/CorrectionDelete/<int:id_correction>', DeleteCorrections.as_view()),

   path('NewspaperDistribution/NewspaperDistributionView/', ViewAllNewspaperDistributions.as_view()),
   path('NewspaperDistribution/NewspaperDistributionCreate/', AddNewspaperDistributions.as_view()),
   path('NewspaperDistribution/NewspaperDistributionEdit/<int:id_newspaper_distribution>', EditNewspaperDistributions.as_view()),
   path('NewspaperDistribution/NewspaperDistributionDelete/<int:id_newspaper_distribution>', DeleteNewspaperDistributions.as_view()),
]