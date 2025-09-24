from .models import Task

class TaskService:

    @staticmethod
    def getOne(pk, user):
        try:
            task = Task.objects.get(pk=pk, user=user)
            return task
        except Task.DoesNotExist as error:
            return None

    @staticmethod
    def userTasks(user):
        tasks = Task.objects.filter(user=user)
        return tasks

    @staticmethod
    def deleteTask(pk, user):
        try:
            task = Task.objects.get(pk=pk, user=user)
            task.delete()
            return True
        except Task.DoesNotExist as error:
            return None