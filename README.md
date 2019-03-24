### Running tests

```
python manage.py test stackoverflow/apps/

```

### Running the app

```
python manage.py runserver
```

### Endpoints

This API has two apps the

1. Questions app
2. Comments app

A comment is like an answer in the real world.

| endpoint             | Description                             |     |     |     |
| -------------------- | --------------------------------------- | --- | --- | --- |
| /questions/          | Get all questions                       |     |     |     |
| /questions/<int:id>/ | Get specific question with all comments |     |     |     |
| /comments/           | Get all comments of all questions       |     |     |     |
