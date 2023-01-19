Polling Application

DRF API : open thunder client vscode extension

```
GET   localhost:8000/api/polls/choice
GET 	 localhost:8000/api/polls/polls
```

Celery :

    used pip install django-celery-beat

to run django celery

    download redis in windows :

    `"https://objects.githubusercontent.com/github-production-release-asset-2e65be/3402186/124bda0a-3fa5-11e6-8c4a-803581ed704c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230118%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230118T140043Z&X-Amz-Expires=300&X-Amz-Signature=2eeb616a9747c435e90fc30f2eb8aa5cf22b749a26fd67fe50bc9c4f0de42198&X-Amz-SignedHeaders=host&actor_id=86487990&key_id=0&repo_id=3402186&response-content-disposition=attachment%3B%20filename%3DRedis-x64-3.0.504.msi&response-content-type=application%2Foctet-stream "`

open redis and type ping> pong

run in cmd :

    celery -A pollme worker --pool=solo -l INFO

    celery -A pollme beat -S django

if not then :

    pip install gevent

    celery -A pollme worker -l info -P gevent
