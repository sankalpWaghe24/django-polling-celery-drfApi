from celery.schedules import crontab

# from celery.task import periodic_task
from django.utils import timezone


from celery import shared_task
from polls.models import Foo


@shared_task(name="delete_expire_polls")
def delete_old_foos():
    # Query all the foos in our database
    foos = Foo.objects.all()

    # Iterate through them
    for foo in foos:

        # If the expiration date is bigger than now delete it
        if foo.expiration_date < timezone.now():
            foo.delete()
            # log deletion
    return "completed deleting foos at {}".format(timezone.now())
