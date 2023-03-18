# Server

Server side of the application.

## Database migrations

Generate migration:

```
flask db migrate [--message MESSAGE] [--sql] [--head HEAD] [--splice] [--branch-label BRANCH_LABEL] [--version-path VERSION_PATH] [--rev-id REV_ID]
```

Apply the changes described by the migration script to database:

```
flask db upgrade [--sql] [--tag TAG] [--x-arg ARG] <revision>
```

Revert changes described by the migration script to database:

```
flask db downgrade [--sql] [--tag TAG] [--x-arg ARG] <revision>
```
