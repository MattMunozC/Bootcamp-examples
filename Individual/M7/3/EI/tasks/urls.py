from django.urls import path
from tasks.views import new_task,full_task,delete_task,edit_task
urlpatterns = [
    path("new_task",new_task),
    path("<task_name>/borrar",delete_task),
    path("<task_name>/editar",edit_task),
    path("<task_name>",full_task)
    # Include other view modules
]